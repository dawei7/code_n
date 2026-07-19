## General
This problem requires **dense ranking**. Equal scores share a rank, and moving to the next lower distinct score increases the rank by exactly one, regardless of how many tied rows came before it.

`DENSE_RANK() OVER (ORDER BY score DESC)` implements those rules directly. The window order determines rank values but does not guarantee the final presentation order, so the outer query should also order by score descending. A stable secondary key such as `id` may make tied rows deterministic without including it in the window order; including `id` inside the window would break ties and assign different ranks.

For `4.00, 4.00, 3.85, 3.65, 3.65, 3.50`, the window encounters four distinct score levels. Both `4.00` rows receive rank 1; the next distinct level receives 2 rather than 3; both `3.65` rows receive 3; and `3.50` receives 4.

The distinction among SQL ranking functions is essential:

- `ROW_NUMBER()` assigns a unique position to every row, so tied scores differ.
- `RANK()` shares ranks across ties but leaves gaps afterward.
- `DENSE_RANK()` shares ranks and leaves no gaps, matching this contract.

Descending window order encounters score values from greatest to least. `DENSE_RANK` starts at one and increments exactly when the ordering value changes, so a row's rank is one plus the number of distinct scores greater than its score. This is precisely the required dense-rank definition. Because window functions retain every original row, all tied rows remain present and receive the same value. The outer ordering then presents the complete correct result from highest to lowest.

## Complexity detail
Without an appropriate index, the engine generally sorts `n` rows for $O(n \log n)$ work and may use $O(n)$ sorting/window storage. An index ordered by score can reduce or eliminate explicit sorting, subject to the query optimizer.

## Alternatives and edge cases
- A correlated subquery can compute `1 + COUNT(DISTINCT higher_score)` for every row, but may perform $O(n^2)$ comparisons without decorrelation or indexing.
- `RANK` and `ROW_NUMBER` have different tie semantics and are not interchangeable with `DENSE_RANK` here.
- All-equal scores all receive rank one. A single row also receives rank one.
- Fractional, zero, or negative scores follow ordinary numeric descending order.
- A secondary output sort key may stabilize ties, but it must not participate in the rank window.
