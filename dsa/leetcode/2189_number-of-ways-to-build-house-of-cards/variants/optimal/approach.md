## General

A row with $t$ triangles uses two leaning cards per triangle and one horizontal card between each adjacent pair. Its card cost is

$$
2t+(t-1)=3t-1.
$$

For $t=1,2,3,\ldots$, possible row costs are therefore

$$
2,5,8,11,\ldots
$$

The exact solution counts subsets of these distinct row costs whose sum is `n`. It does so with a memoized include-or-skip recursion.

The manifest describes a descending one-dimensional DP, which is an alternative implementation of the same subset-counting idea. The protected source uses recursion and a two-argument cache.

**Why row triangle counts must be distinct**

A row with $b$ triangles has $b-1$ horizontal cards. Those are the only supports available for triangles in the row immediately above it.

Therefore an upper row can contain at most $b-1$ triangles, strictly fewer than the lower row. Triangle counts decrease as the house rises.

Conversely, if distinct positive triangle counts are chosen, arranging them from largest on the bottom to smallest on top gives the only possible order. The “leftmost available spot” rule removes horizontal-placement choices.

Thus a house corresponds exactly to a set of distinct positive triangle counts, or equivalently a subset of the distinct costs `3t - 1`.

**Map recursion index `k` to one row choice**

In `dfs(n, k)`, parameter `n` is the number of cards still unassigned, while `k` identifies the next possible triangle count.

The expression `x = 3 * k + 2` equals

$$
3(k+1)-1,
$$

so it is the cost of a row with `k + 1` triangles. At `k = 0` the first candidate costs two, then five, then eight.

Increasing `k` ensures a row size is considered at most once. This enforces distinct triangle counts automatically.

**Choose whether to include the candidate row**

When `x < n`, the recursion has two disjoint choices:

- include this row, leaving `n - x` cards and advancing to `k + 1`;
- skip this row, leaving `n` cards and also advancing to `k + 1`.

The returned sum

`dfs(n - x, k + 1) + dfs(n, k + 1)`

counts both groups of houses. They cannot overlap because one group contains the row of cost `x` and the other does not.

**Handle exact completion**

If `x == n`, selecting this row uses all remaining cards and completes exactly one subset.

The function returns one immediately rather than also exploring the skip branch. Every future row cost is larger than `x`, so after skipping, no later single cost or positive combination could sum to the smaller remaining amount `n = x`. The omitted skip branch would contribute zero.

**Prune an oversized candidate**

If `x > n`, the current row cannot fit. All later candidate costs are even larger because the sequence increases by three.

No completion is possible from this state, so the function returns zero. This monotonicity makes the base case conclusive.

**Cache repeated subproblems**

Different include-and-skip paths can reach the same pair of remaining cards and next candidate index. `@cache` stores the computed result for each `(n, k)` pair.

Without caching, the recursion would repeatedly explore the same suffix of row choices and grow exponentially. With caching, each distinct state is evaluated once and later calls reuse its integer result.

**Why each house is counted exactly once**

Take any valid house. Convert each row's triangle count $t$ to candidate index `k = t - 1`. As recursion visits indices in ascending order, follow the include branch exactly at those indices and the skip branch at all others. The selected costs sum to the original card count, so this unique path reaches an exact-completion return of one.

Conversely, every path counted as one selects distinct candidate costs summing to `n`. Those costs correspond to distinct row triangle counts. Ordering them largest to smallest constructs a valid supported house, and the leftmost rule makes its shape unique.

No two paths select the same subset because the include-or-skip decision at the first differing index distinguishes them. Hence the returned count equals the number of distinct houses.

For `n = 2`, candidate cost two matches immediately and returns one. For `n = 4`, cost two can be selected but leaves two while all later costs are at least five, and skipping two also leaves no fitting cost, so the result is zero.

## Complexity detail

The remaining-card value ranges from zero through the original $n$, and `k` ranges over $O(n)$ possible row costs before `3k+2` exceeds $n$. This gives an $O(n^2)$ upper bound on cached states. Each state performs constant work besides cached calls, so time is $O(n^2)$.

The exact cache can also store $O(n^2)$ state results. Recursion depth is $O(n)$ because `k` increases on every call. Therefore exact auxiliary space is $O(n^2)$, dominated by the cache.

The manifest's $O(n)$ space applies to a descending one-dimensional subset-sum DP, not this memoized two-parameter implementation. Its $O(n^2)$ time remains a valid broad bound for the source.

## Alternatives and edge cases

- **Descending one-dimensional DP:** For every row cost, update card totals from `n` downward. This counts each cost once and uses $O(n)$ space, matching the manifest.
- **Two-dimensional tabulation:** Store counts by candidate prefix and card total. It mirrors the recursion but also uses $O(n^2)$ space.
- **Uncached recursion:** Include-or-skip logic remains correct but repeats subproblems exponentially.
- **Single triangle:** It costs two cards and forms the unique house for `n = 2`.
- **Too few cards:** `n = 1` cannot fit the smallest cost, so the answer is zero.
- **Exact candidate cost:** Returning one is sufficient because all skipped future costs are larger.
- **Distinct rows:** Advancing `k` after inclusion prevents reusing a triangle count.
- **Row ordering:** A chosen subset has one valid bottom-to-top order: decreasing triangle counts.
- **Leftmost placement:** It prevents multiple horizontal arrangements from creating extra counts for the same row sizes.
- **All cards required:** Only paths whose selected costs sum exactly to the input contribute.
- **No modulo:** The contract requests the exact count, and Python integers can grow without overflow.
- **Cache key:** Both remaining cards and next candidate matter; caching by only one would merge different choice sets incorrectly.
- **Manifest discrepancy:** The exact source uses memoized recursion and quadratic cache space rather than a one-dimensional iterative array.
