## General

**Solve each string position independently.** An operation changes one selected character and has no effect on any other index. There is no shared operation budget or cross-position discount. Therefore the minimum total cost is the sum of the minimum conversion cost for every pair `(s[i], t[i])`.

For one source letter and target letter, the alphabet is a cycle of 26 vertices. There are two direct routes:

- repeatedly take the next-letter edge;
- repeatedly take the previous-letter edge.

All costs are nonnegative. Any route that changes direction contains avoidable backtracking, and any extra full cycle adds nonnegative cost. Thus an optimal route is one of those two simple directional paths.

**Duplicate the alphabet to remove wraparound cases.** Letter indices run from 0 for `'a'` through 25 for `'z'`. The source conceptually places two copies of that cycle in a line, with indices 0 through 51. A wrapped path can then be represented as an ordinary forward interval in this doubled sequence.

Expression `m << 1 | 1` produces 53 when `m = 26`, so `s1` and `s2` have indices 0 through 52. The loop fills 52 edge contributions and their prefix endpoints.

**Build forward-route prefix costs.** Moving forward from letter index $j$ to $j+1$ costs `nextCost[j]`. The recurrence

`s1[i + 1] = s1[i] + nextCost[i % 26]`

stores cumulative next-edge costs across two alphabet copies.

For source index `x` and target index `y`:

- when `y >= x`, the forward cost is `s1[y] - s1[x]`;
- when `y < x`, the route wraps through `z -> a`, so target position `y + 26` is used.

The combined code is

`c1 = s1[y + m if y < x else y] - s1[x]`.

**Build backward-route prefix costs with shifted indexing.** Moving backward from letter $j$ to $j-1$ costs `previousCost[j]`. To make a prefix difference over increasing doubled indices represent this reverse traversal, the source adds

`previousCost[(i + 1) % 26]`

between `s2[i]` and `s2[i + 1]`.

Consequently, `s2[x] - s2[y]` for `x >= y` sums `previousCost[y+1]` through `previousCost[x]`, exactly the costs of moving backward from $x$ down to $y$. If `x < y`, adding 26 to `x` represents wrapping backward through `a -> z`:

`c2 = s2[x + m if x < y else x] - s2[y]`.

**Check a single wraparound edge.** Converting `'z'` to `'a'` forward has `x=25` and `y=0`. The source uses `s1[26] - s1[25]`, which contains only `nextCost[25]`. Converting `'a'` to `'z'` backward uses `s2[26] - s2[25]` and extracts `previousCost[0]`. These are exactly the statement's wrap costs.

**Choose the cheaper direction for each character.** The source adds `min(c1, c2)` to `ans`. Because indices are independent, selecting the minimum separately cannot conflict with any other selection and yields the minimum possible total.

**Why mixed-direction walks cannot improve the result.** Suppose a walk moves forward and later immediately retraces some alphabet edge backward, or vice versa. Removing that detour leaves the same current letter and cannot increase cost because both removed edges have nonnegative costs. Repeating this cancellation transforms any optimal walk into a direction-consistent simple route, possibly after removing full cycles. The two computed routes therefore cover an optimum even when edge costs vary greatly.

This matters in examples where 25 cheap steps beat one expensive step. The algorithm compares total directional costs rather than assuming fewer operations is cheaper.

**Same-letter conversion.** When `x == y`, both prefix differences are zero. The algorithm correctly spends nothing; taking a full cycle could have zero cost in some inputs but can never improve below zero.

**Why the accumulated answer is exact.** Prefix differences include every edge of each direct circular route once, with the correct cost associated with the letter being departed. The minimum selects the optimal route for one position. Summation then combines independent per-position optima, which is exactly the global shift distance.

## Complexity detail

Let $n$ be the common string length and $A=26$ the alphabet size. Building the doubled prefix arrays costs $O(A)$ time. Processing the zipped character pairs costs $O(n)$ time, so total time is $O(n+A)=O(n)$.

The two arrays contain $2A+1=53$ integers. Space is $O(A)$ in a generalized alphabet analysis and $O(1)$ for the fixed lowercase-English alphabet, matching the manifest. Python integers safely hold totals beyond 32-bit range.

## Alternatives and edge cases

- **Simulate both routes per character:** At most 25 steps in each direction still gives $O(26n)$ time, asymptotically linear but with repeated cost summation.
- **All-pairs shortest paths:** Floyd–Warshall on 26 letters works but ignores the simple cycle structure and costs $O(26^3)$ preprocessing.
- **Dijkstra per letter pair:** Nonnegative weights permit it, but two simple routes are the only candidates after removing backtracking.
- **Forward wrap:** Use target index `y+26` when `y<x`.
- **Backward wrap:** Use source index `x+26` when `x<y`.
- **Same source and target:** Both costs are zero.
- **Zero-cost edges:** A long route may be free and must be compared rather than rejected for using more shifts.
- **Highly asymmetric costs:** Forward and backward arrays are independent; neither direction is assumed cheaper.
- **Cost belongs to the current letter:** Forward uses `nextCost[j]` when leaving $j$, while backward uses `previousCost[j]` when leaving $j$.
- **Shifted `s2` index:** The `(i+1) % 26` term is deliberate and aligns reverse-edge costs with prefix subtraction.
- **Equal string lengths:** `zip` processes every position because the contract guarantees equal lengths.
- **Lowercase-only contract:** Ordinal subtraction maps every character safely into 0 through 25.
- **Large costs and long strings:** The total may exceed 64-bit limits in other languages; Python's integer arithmetic remains exact.
- **Input preservation:** Strings and cost arrays are read only.
- **No benefit from full cycles:** Costs are nonnegative, so adding a cycle cannot lower a route's total.
