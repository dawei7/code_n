## General

**Preserve the complete salesperson set.** Begin with `Salesperson` and left-join `Customer` by `salesperson_id`. An inner join would discard a salesperson with no customers, even though the required output must include that row with a zero total.

**Carry empty customer histories through the second join.** Left-join `Sales` by `customer_id`. This retains both a salesperson without customers and a salesperson whose customers have no sales. For a salesperson with sales, the joined rows contain every relevant `price` exactly once.

Group by the salesperson identifier and name, then sum `price`. SQL's `SUM` returns `NULL` when a group has no non-null prices, so wrap it in `COALESCE(..., 0)`. The aggregation therefore returns the complete set of salespeople with the required influence value.

The contract permits any row order. Ordering by `salesperson_id` is harmless and gives deterministic output for the local execution harness.

## Complexity detail

Let $S$, $C$, and $R$ be the row counts of `Salesperson`, `Customer`, and `Sales`. A conservative sort-based bound for the joins, grouping, and final ordering is $O((S+C+R)\log(S+C+R))$ time with $O(S+C+R)$ working space. Hash joins, hash aggregation, and useful indexes can make the main data pass closer to linear in practice.

## Alternatives and edge cases

- **Preaggregate by salesperson:** Joining `Customer` to `Sales`, grouping those rows, and then left-joining the totals to `Salesperson` is equivalent and can reduce intermediate rows.
- **Correlated subquery:** Summing matching sales separately for every salesperson is correct but may repeatedly rescan customer and sale rows, producing quadratic work.
- **No customers:** The first left join must retain the salesperson.
- **Customers without sales:** The second left join must also be outer so the final total becomes `0`.
- **Multiple customers and sales:** Group only after joining through customer ownership so every price contributes to the correct salesperson.
- **Null aggregate:** `SUM` over no prices is `NULL`; `COALESCE` is required by the zero-total rule.
