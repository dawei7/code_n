## General
**Filter bills at the strict threshold**

Apply `WHERE amount > 500` before aggregation. This retains every bill that can establish a rich customer and rejects both lower amounts and the boundary value 500. A customer with any retained row qualifies regardless of their other bills.

**Count customers rather than bills**

Use `COUNT(DISTINCT customer_id)` over the filtered relation. `DISTINCT` collapses all qualifying bills for one customer to one identity before counting, directly matching the “at least one bill” condition. The aggregate returns one row even when no bill qualifies, in which case the count is zero.

**Name the scalar result exactly**

Alias the aggregate as `rich_count`. No grouping is needed because the requested result is one total across the complete table, and no ordering clause is relevant to a single-row relation.

## Complexity detail
The filter reads $B$ rows. A sort-based implementation of `COUNT(DISTINCT ...)` takes $O(B\log B)$ time and stores up to $O(C)$ qualifying customer identities; a hash aggregate can achieve expected $O(B)$ time with the same asymptotic identity storage. Database indexes and optimizer choices may alter the physical plan without changing the query semantics.

## Alternatives and edge cases
- **Group then count:** Selecting qualifying customers with `GROUP BY customer_id` in a subquery and applying `COUNT(*)` outside is equivalent but more verbose.
- **Count qualifying rows:** `COUNT(*)` after the filter is wrong when one customer has several bills above 500.
- **Conditional distinct aggregate:** `COUNT(DISTINCT CASE WHEN amount > 500 THEN customer_id END)` is equivalent because `COUNT` ignores nulls.
- **Exact threshold:** An amount of 500 is excluded by the strictly-greater comparison.
- **Mixed bills for one customer:** One qualifying bill is sufficient even when the same customer also has nonqualifying bills.
- **No qualifying rows:** The aggregate still returns `rich_count = 0`.
