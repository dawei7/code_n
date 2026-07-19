## General
**Count transactions without losing empty visits**

Left join `Visits` to `Transactions` on both `user_id` and the matching date. Group by the visit's composite key and use `COUNT(transaction_date)`. Counting a nullable column, rather than `COUNT(*)`, gives zero for a visit whose left join produced only the placeholder row.

**Generate the complete bucket range**

Find the largest per-visit count. A recursive common table expression starts at 0 and emits the next integer until it reaches that maximum. Left join this generated series to the per-visit counts, group by the generated integer, and count matching visits. Because the series is the preserved side, transaction counts that never occur still produce a row with zero.

Finally, order by the generated count. Every visit contributes to exactly one bucket because its transaction count was computed once from its matching rows, and the complete integer series proves that no required gap can disappear.

## Complexity detail
With indexed or sort-based grouping, joining and aggregating $N$ input rows takes $O(N\log N)$ time in the general comparison model. Generating and aggregating at most $T+1$ buckets stays within that bound. The grouped visits, bucket series, and database working structures use $O(N)$ space.

## Alternatives and edge cases
- **Correlated count per visit:** Counting matching `Transactions` in a scalar subquery is concise but may rescan all $T$ transactions for each visit, taking $O(VT)$ time.
- **Group transactions before joining:** Pre-aggregating by user and date is also efficient, provided the subsequent left join preserves visits with no match.
- **No transactions:** The maximum visit count is zero, so the output still contains the single bucket `[0, V]`.
- **Missing intermediate count:** Generate it explicitly and report zero visits.
- **Composite match:** Equal dates from different users, or different dates for one user, must not be combined.
- **Duplicate transaction rows:** Each row represents a separate transaction and contributes to the visit's count.
- **Unmatched transaction:** A transaction with no corresponding visit does not create a visit or a bucket contribution.
