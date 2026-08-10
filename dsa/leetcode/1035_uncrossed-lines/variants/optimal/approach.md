## General

**Uncrossed lines are a common subsequence**

Suppose one line connects `nums1[i_1]` to `nums2[j_1]` and another connects `nums1[i_2]` to `nums2[j_2]`. If `i_1 < i_2` but `j_1 > j_2`, the endpoints appear in opposite orders on the two horizontal rows, so the lines cross.

Therefore, any valid set of lines has indices increasing in both arrays:

$$
i_1<i_2<\cdots
\quad\text{and}\quad
j_1<j_2<\cdots.
$$

Every connected pair must also have equal values. Reading the connected values from left to right produces a sequence that appears in order in both arrays: a common subsequence.

The equivalence works in the other direction too. Given any common subsequence, connect the corresponding increasing indices. Equal values satisfy the connection rule, no index is reused, and consistent endpoint order prevents crossings.

Thus the maximum number of uncrossed lines is exactly the length of the longest common subsequence, usually abbreviated LCS.

**Define prefix subproblems**

Let `f[i][j]` be the maximum lines possible using only the first `i` values of `nums1` and the first `j` values of `nums2`.

The table has `m + 1` rows and `n + 1` columns. Row zero or column zero represents an empty prefix. No line can be drawn when either side has no values, so those states correctly remain zero after initialization.

Using prefix lengths rather than zero-based element indices makes the recurrence clean: the final values of state `f[i][j]` are `nums1[i - 1]` and `nums2[j - 1]`.

The exact loops use `enumerate(nums1, 1)` and `enumerate(nums2, 1)`, so `i` and `j` already have these one-based prefix meanings while `x` and `y` hold the actual final values.

**When the final values match**

If `x == y`, the two final values can be connected. Removing that line leaves a valid uncrossed solution using the first `i - 1` and `j - 1` values. Therefore,

`f[i][j] = f[i - 1][j - 1] + 1`.

Why is it safe to take this match rather than also checking skip cases? Because equal final values can be placed as the last pair after an optimal common subsequence of the two shorter prefixes. They occur later than every index used by that shorter solution, so the added line cannot cross.

The standard LCS argument also shows no better solution is lost. Any common subsequence of the two current prefixes either uses these equal final elements, leaving a subsequence of the shorter prefixes, or can be adjusted so that its last occurrence of this shared value uses the final positions without shortening it. Thus the diagonal optimum plus one attains the prefix optimum.

**When the final values differ**

If `x != y`, they cannot be connected to each other. Any valid solution for the two prefixes must omit at least one of them:

- Ignore `x` and use state `f[i - 1][j]`.
- Ignore `y` and use state `f[i][j - 1]`.

The better of those possibilities is optimal:

`f[i][j] = max(f[i - 1][j], f[i][j - 1])`.

This does not mean both final values are permanently discarded. Each smaller state may still match one of them with an earlier equal value on the opposite side.

**Why table fill order satisfies dependencies**

The loops process rows from top to bottom and columns from left to right. When calculating `f[i][j]`:

- `f[i - 1][j - 1]` is in the previous row.
- `f[i - 1][j]` is in the previous row.
- `f[i][j - 1]` was calculated earlier in the current row.

Every required state is already final. No recursion or revisiting is necessary.

**Trace the first example**

For `nums1 = [1,4,2]` and `nums2 = [1,2,4]`, the first values match, so the table records one line for the two length-one prefixes.

Later, value four in `nums1` can match the final four in `nums2`, producing common subsequence `[1,4]`. Alternatively, value two in `nums1` can match the middle two in `nums2`, producing `[1,2]`.

Trying to take both four and two would use their indices in order `4` then `2` in the first array but `2` then `4` in the second. The corresponding lines cross. The DP's prefix choices retain the better noncrossing alternative and return two.

**Why endpoint reuse is automatically prevented**

When values match, the transition moves diagonally to `i - 1, j - 1`. Both matched endpoints are removed from the remaining subproblem, so neither can be used again.

When values differ, moving up or left removes at least one endpoint from consideration. Every reconstructed sequence of transitions uses strictly increasing indices in forward order, satisfying the rule that lines cannot intersect at a shared endpoint.

**Why the final cell is the answer**

The recurrence considers every way an optimal prefix solution can relate to its two final elements: pair them when equal, or omit at least one when different. The zero row and column are correct base cases.

By induction on the pair of prefix lengths, every `f[i][j]` equals the LCS length for those prefixes. `f[m][n]` covers both full arrays. By the geometric equivalence, it is also exactly the maximum number of uncrossed lines.

**Why greedy matching is unsafe**

Matching the first equal value seen can consume an occurrence needed to preserve more future matches. Repeated values create choices whose quality depends on both remaining suffixes. The DP keeps the best result for every prefix pair instead of committing without enough information.

## Complexity detail

Let `M = len(nums1)` and `N = len(nums2)`. The nested loops fill `MN` interior states, each with constant work. Initializing the table has the same order of work. Total time is `O(MN)`, matching the manifest.

The exact solution allocates an `(M + 1) \times (N + 1)` table, so its actual auxiliary space is `O(MN)`.

The manifest lists the optimized target `O(\min(M,N))`. That bound is achievable because a row depends only on the preceding row and its current left neighbor, but the exact provided source has not applied that compression. An accurate reading of this implementation must therefore distinguish its `O(MN)` table from the one-dimensional optimization described below.

## Alternatives and edge cases

- **One-dimensional LCS table:** Make the shorter array the column dimension and keep one row, preserving the old diagonal value in a scalar while updating left to right. This retains `O(MN)` time and reaches the manifest's `O(\min(M,N))` space target.
- **Two rolling rows:** Store previous and current rows instead of the full table. It is easier to reason about than in-place one-row updates and uses `O(N)` space.
- **Memoized recursion:** Recursively solve prefix or suffix pairs and cache results. It has the same `O(MN)` state count but adds call-stack overhead.
- **Greedy nearest equal match:** Choosing the earliest available equal value can block a longer alignment later, especially with duplicates. LCS dynamic programming handles those competing choices.
- **Build all line sets:** Enumerating match subsets is exponential and unnecessary because prefix states summarize their best sizes.
- **One-element arrays:** The answer is one if the values match and zero otherwise; the first table state implements exactly that.
- **No shared values:** Every comparison uses the unequal recurrence, and the final answer remains zero.
- **Identical arrays:** Every corresponding pair matches along the diagonal, so the answer is the full length.
- **Repeated values:** Different occurrences remain distinct endpoints. Prefix indices let the DP choose the order-preserving combination.
- **Different array lengths:** The rectangular table handles them directly; no padding or special case is needed.
- **Crossing temptation:** Matches `i_1 < i_2` and `j_1 > j_2` cannot coexist. The common-subsequence ordering excludes them automatically.
- **Touching endpoints:** A single array index cannot be reused because each match consumes one index from each prefix through a diagonal transition.
- **Space-bound discrepancy:** The exact code is a full-table implementation. Claiming it uses `O(\min(M,N))` would be inaccurate unless the storage is rewritten to rolling rows or one dimension.
- **Recovering actual lines:** The full table could be backtracked to reconstruct matched index pairs, but the problem requests only the maximum count, so the method returns one integer.
