## General

**Keep as much of target as already appears in order**

If a subsequence of `target` already occurs in `arr`, those matched elements need no insertion. Every target element not in that matched subsequence can be inserted at the appropriate point around the matches.

Therefore, if the longest common subsequence length is $L$, the minimum operations equal

$$
\lvert\texttt{target}\rvert-L.
$$

The challenge is finding $L$ efficiently for arrays up to $10^5$.

**Exploit the distinct target values**

The source maps every target value to its one-based position:

`d = {x: i for i, x in enumerate(target, 1)}`.

Because `target` has no duplicates, every relevant value has one unambiguous position. It then filters `arr` to values present in `d` and replaces each by that position:

`nums = [d[x] for x in arr if x in d]`.

Any subsequence of `arr` that matches target order becomes a strictly increasing subsequence of `nums`. Conversely, any strictly increasing subsequence of positions names values appearing in target order and therefore corresponds to a common subsequence.

The longest common subsequence problem has thus become a longest strictly increasing subsequence problem.

**Why duplicates in arr require strict increase**

`arr` may repeat a value. Each occurrence maps to the same target position. A target element can be matched only once because target contains that value once. A non-decreasing subsequence could incorrectly use repeated equal positions, but a strictly increasing subsequence cannot.

The exact source enforces strictness by querying only positions less than `x` when processing mapped position `x`.

**Store prefix-best LIS lengths in a Fenwick tree**

`BinaryIndexedTree` has size `m = len(target)`. Unlike the common sum Fenwick tree, this one stores maximum values.

Conceptually, after processing some mapped elements, a prefix query `query(x)` returns the greatest LIS length whose final target position is at most `x`.

For current position `x`, the best strictly increasing subsequence ending here extends a subsequence ending below it:

`v = tree.query(x - 1) + 1`.

If no smaller position has appeared, the query returns zero and `v` becomes one.

**How the Fenwick query works**

The internal array `c` is one-based. `query(x)` repeatedly reads `c[x]`, combines it with `res` using `max`, and removes the lowest set bit with `x -= x & -x`.

Each visited tree cell summarizes a disjoint suffix block of the remaining prefix. Together those blocks cover positions one through the original `x`, so their maximum is the desired prefix maximum. Removing a lowest set bit strictly decreases `x`, giving logarithmic steps.

**How the Fenwick update works**

`update(x, v)` raises every Fenwick node whose summarized range contains position `x`:

`self.c[x] = max(self.c[x], v)`,

then moves upward with `x += x & -x`.

Using maximum rather than assignment is important. Several `arr` occurrences can map to the same target position, and a later update must not erase a better LIS length already known.

The query happens before the update, and it uses `x-1`. Hence the current occurrence and earlier duplicates at the same position cannot extend one another.

**Track the global best**

`ans = max(ans, v)` records the longest increasing subsequence found anywhere. The Fenwick tree also contains the information, but maintaining `ans` avoids a final full-range query and makes the intended result explicit.

After every mapped value has been processed, `ans` is the LCS length. The source returns `len(target) - ans`.

**Why insertions achieve this lower bound**

At most $L$ target elements can already be preserved in the required order, so any solution must add at least `len(target)-L` missing positions. Starting with an actual LCS, insert each other target value before, between, or after its neighboring matched values. Insertions never disturb the order of existing elements, so exactly that many operations suffice.

The lower and upper bounds match, proving minimality.

## Complexity detail

Let $T$ be `len(target)`, $A$ be `len(arr)`, and $M$ be the number of `arr` elements found in target. Building `d` costs expected $O(T)$ time; filtering and mapping costs expected $O(A)$. Each of the $M$ Fenwick operations costs $O(\log T)$, for total

$$
O(T+A+M\log T),
$$

covered by the manifest's $O(n+m\log n)$ notation when $n=T$ and $m=A$.

The dictionary and tree each use $O(T)$ space. The exact source also materializes `nums` with $M$ entries, so total auxiliary space is $O(T+M)$, or $O(T+A)$ in the worst case. The manifest's plain $O(n)$ space is accurate only if its $n$ denotes the combined input scale or if mapped values are streamed rather than stored.

## Alternatives and edge cases

- **Patience-sorting LIS:** Maintain minimum tails and use binary search for each mapped position. It gives the same $O(A\log T)$ time with simpler $O(T)$ state.
- **Full LCS table:** Standard dynamic programming costs $O(TA)$ time and space, which is infeasible here.
- **Stream mapped positions:** Process each relevant `arr` value immediately instead of building `nums`, reducing the extra $O(M)$ list allocation.
- **No arr value in target:** `nums` is empty, `ans=0`, and every target element must be inserted.
- **Target already a subsequence:** The mapped stream contains an increasing subsequence of length $T$, so the answer is zero.
- **Duplicate arr values:** Equal target positions cannot extend each other because the query ends at `x-1`.
- **Arr values outside target:** They are filtered out because they cannot help form the required subsequence.
- **One target element:** The answer is zero if it appears in arr and one otherwise.
- **One-based mapping:** Fenwick operations require positive indices; `enumerate(target,1)` avoids index zero.
- **Maximum update:** Repeated writes preserve the best length rather than overwriting it with a smaller one.
- **Insertion anywhere:** This freedom is what makes every unmatched target element independently insertable around the retained LCS.
