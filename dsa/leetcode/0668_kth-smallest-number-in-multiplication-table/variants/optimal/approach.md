## General
**Search product values instead of materializing cells**

Every table entry lies between `1` and $m \cdot n$, so the answer can be located within that numeric interval. For any candidate value `x`, ask whether at least `k` table entries are at most `x`. This predicate is monotone: once it becomes true, it remains true for every larger value. Binary search can therefore find its first true value without constructing or sorting the table.

**Count the entries below a candidate row by row**

Row `r` contains `r, 2r, 3r, ..., nr`. The entries no larger than `x` are precisely its first $\left\lfloor x / r \right\rfloor$ products, capped at the row length `n`. Thus row `r` contributes $\min(n, \left\lfloor x / r \right\rfloor)$, and summing this quantity over all rows gives the number of table entries at most `x`. Swapping the dimensions when necessary makes the sum iterate over the smaller dimension while describing the same multiset of products.

**Why the lower bound is exactly the requested rank**

Let `v` be the smallest value whose count is at least `k`. Every value below `v` has fewer than `k` table entries at or below it, so the `k`-th sorted entry cannot be smaller than `v`. At least `k` entries are at most `v`, so the `k`-th entry cannot be larger than `v`. These two facts force the answer to be `v`. The first-true search is important when products repeat: it returns the repeated value covering rank `k`, not a particular cell containing it.

## Complexity detail
After arranging $m \le n$, one counting pass visits $m = \min(M, N)$ rows. Binary search examines $O(\log(MN))$ candidate values, giving $O(\min(M, N) \log(MN))$ time. Only the interval bounds, candidate, count, and loop index are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Staircase counting:** keep a column pointer that only moves left while scanning successive rows; this counts one candidate in $O(M + N)$ time and remains competitive, but the division-based count is simpler and can explicitly use the smaller dimension.
- **Heap merge of sorted rows:** treat every row as a sorted stream and extract the smallest product `k` times; it uses $O(\min(M, N))$ space and $O(k \log \min(M, N))$ time, which depends directly on the requested rank.
- **Materialize and sort the table:** is straightforward and correct, but stores all `MN` products and costs $O(MN \log(MN))$ time.
- Duplicate products must be counted once per cell; for example, both $1 \cdot 2$ and $2 \cdot 1$ contribute to separate ranks.
- When $k = 1$, the answer is `1`; when $k = M \cdot N$, the answer is $M \cdot N$.
- A one-row or one-column table is already an increasing sequence, and the same lower-bound search still applies.
