## General

A trionic array must follow exactly three nonempty edge phases:

1. strictly increasing;
2. strictly decreasing;
3. strictly increasing.

The source greedily consumes the maximal prefix for each required phase. If anything remains after the third phase, or any phase has no comparison, the array is not trionic.

**First increasing phase**

`p` begins at index 0. While:

`nums[p] < nums[p+1]`

the phase continues and `p` moves right.

The condition `p<n-2` ensures at least two later edges remain available in principle for a decreasing and final increasing phase.

After the loop, p is the peak where the first increasing run ends.

If `p==0`, the first pair was not strictly increasing, so the required first segment has fewer than two elements. The method returns false.

**Decreasing phase**

`q` starts at p and advances while:

`nums[q] > nums[q+1]`.

If `q==p`, no decreasing edge occurred. The middle segment is invalid.

If `q==n-1`, the decreasing run consumed the rest of the array, leaving no final increasing edge. The method also returns false.

After these checks, q is a valid valley satisfying `0<p<q<n-1`.

**Final increasing phase**

The last loop advances q while consecutive values strictly increase.

The final condition `q==n-1` succeeds only if this third increasing phase consumes every remaining edge. If it stops early because of equality or another decrease, the array has an invalid fourth phase or non-strict step.

**Why maximal greedy phases are correct**

The first turning index p is forced. As long as consecutive values increase, choosing an earlier p would make the next decreasing segment start with an increasing edge, violating strict decrease. When the first non-increasing edge arrives, p cannot move farther while preserving the first phase.

The same reasoning forces q: every consecutive decrease belongs to the middle phase, and choosing q before that run ends would make the final phase begin with a decreasing edge.

Therefore, if valid p and q exist, they must be exactly the maximal-run boundaries found by the source. No backtracking or alternative split is needed.

**Equality is always invalid**

All three phases are strict. If two adjacent values are equal, neither the increasing nor decreasing loop consumes that edge.

If equality occurs at a proposed turn, the next required phase also cannot consume it, so the final endpoint check fails. Equality anywhere makes the whole array non-trionic.

**Following the valid example**

For `[1,3,5,4,2,6]`:

- p advances from 0 to 2 through 1<3<5;
- q advances from 2 to 4 through 5>4>2;
- the final loop advances from 4 to 5 through 2<6.

All three phases contain an edge and q reaches n-1, so the method returns true.

**Following a too-short pattern**

For `[2,1,3]`, p remains zero because 2<1 is false. The first increasing segment is missing, so the method returns false immediately.

In fact, the strict inequalities `0<p<q<n-1` require at least four elements. Length-three inputs always fail, even though the broad constraints allow them.


If the method returns true, p>0 proves a nonempty strictly increasing prefix. q>p proves a nonempty strictly decreasing middle. q was below n-1 before the last loop, and reaching n-1 through strict increases proves a nonempty final phase. The indices satisfy every contract condition.

Conversely, suppose the array is trionic. Its first valid p must be the end of the maximal initial increasing run, so the first loop finds it. Its q must be the end of the following maximal decreasing run, so the second loop finds it. The remaining suffix is strictly increasing, so the third loop reaches n-1. None of the rejection checks fires, and the source returns true.

## Complexity detail

Each pointer only moves right. Although there are three loops, together they inspect each adjacent pair at most once. Time complexity is `O(n)`.

Only n, p, and q are stored. The method allocates no arrays, sets, or recursion stack, so auxiliary space is `O(1)`.

## Alternatives and edge cases

- **Count sign changes:** Reject zero differences and require edge signs `+,-,+` with exactly two turns. This matches the second editorial approach.
- **Try every p and q:** It is unnecessary and can cost `O(n^3)` with repeated segment checks.
- **Length three:** No indices can satisfy `0<p<q<n-1`, so false.
- **Exactly four values:** Each phase must contain exactly one edge.
- **Entirely increasing:** No decreasing phase, so false.
- **Entirely decreasing:** The first phase is missing, so false.
- **Increase then decrease only:** q reaches n-1 and is rejected for lacking the final phase.
- **Decrease then increase:** p remains zero and is rejected.
- **Equality anywhere:** Strict monotonicity fails.
- **Extra fourth turn:** The final increasing loop stops before n-1, so false.
- **Negative values:** Only comparisons matter; signs and magnitudes do not.
- **Turning-point elements:** nums[p] belongs to both first and second segments, and nums[q] belongs to middle and final segments, as required by inclusive ranges.
- **Input preservation:** The source only reads `nums`.
- **Missing `List` import:** Standalone execution must provide the annotation name.
