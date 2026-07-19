## General
The requested rank belongs to salary **values**, not employee rows. Begin by reducing the salaries to a distinct relation; otherwise three employees earning the maximum would incorrectly occupy the first three positions.

Order those distinct values from highest to lowest. In that sequence, one-based rank `N` is at zero-based offset $N - 1$. The native MySQL function can adjust its parameter to that offset and select one row with `LIMIT`. The app-local SQL fixture expresses the same operation using `Request(N)`.

The selected row should be evaluated as a scalar subquery. A scalar subquery returns `NULL` when it produces no row, which is exactly the required outcome when the number of distinct salaries is smaller than `N`. Without that wrapper, an offset beyond the data would produce an empty result set rather than one result row containing null.

For salaries `300, 300, 200, 100` and $N = 2$, deduplication gives `300, 200, 100`; descending offset one selects `200`. The duplicate maximum never changes any rank.

After `DISTINCT`, each salary value appears exactly once. Descending order places precisely $N - 1$ greater distinct salaries before the value at offset $N - 1$, so that value is the Nth-highest distinct salary. If the offset does not exist, fewer than `N` distinct values are present, and scalar-subquery null semantics return the specified fallback. Thus the query is correct in both the present and absent-rank cases.

## Complexity detail
Without a supporting index, deduplicating and sorting `n` salaries requires $O(n \log n)$ logical work and up to $O(n)$ intermediate storage. A suitable salary index may let the engine obtain distinct values in descending order more efficiently; physical costs remain optimizer-dependent.

## Alternatives and edge cases
- `DENSE_RANK()` expresses the definition directly, but the query must still isolate rank `N` and preserve one-row null behavior.
- Counting distinct greater salaries can avoid an explicit offset, though a correlated formulation may be quadratic without optimization.
- Repeated nested `MAX` queries work for a fixed small rank but do not generalize cleanly to arbitrary `N`.
- Omitting `DISTINCT` ranks employees rather than salary levels and is incorrect when salaries repeat.
- `N` is positive and one-based. $N = 1$ requests the maximum; an empty or undersized distinct set yields `NULL`.
