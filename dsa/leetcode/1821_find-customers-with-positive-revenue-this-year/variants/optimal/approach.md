## General
**Apply both qualifications to the same table row**

Read `Customers` once and retain a row only when its `year` equals 2021 and its `revenue` is strictly greater than zero. These predicates must be joined with `AND`: satisfying only the year condition or only the revenue condition is insufficient.

**Project only the requested identifier**

Select `customer_id` from the qualifying rows. The `(customer_id, year)` key guarantees at most one 2021 row for each customer, so the filter cannot produce duplicate identifiers and no `DISTINCT`, grouping, join, or aggregation is required.

**Why the result is exact**

Every returned row comes from 2021 and has positive revenue because it passes both predicates. Conversely, every customer meeting the definition has a corresponding table row that passes those same predicates and is therefore returned. Rows for other years cannot influence the decision about the 2021 row.

## Complexity detail
Without assuming a particular index, the database scans the $r$ table rows once and evaluates two constant-time predicates, giving $O(r)$ time. The result contains $o$ identifiers and therefore uses $O(o)$ output space; the query requires no additional relation proportional to the input.

## Alternatives and edge cases
- **Filter only positive revenue:** This incorrectly includes customers whose positive revenue occurred outside 2021.
- **Filter only the year:** This incorrectly includes zero and negative revenue.
- **Group by customer and sum revenue:** There is already at most one row per customer-year, and combining other years changes the required semantics.
- **Self-join or correlated subquery:** These can reproduce the filter but add unnecessary repeated table work.
- **Zero revenue:** The comparison is strict, so zero does not qualify.
- **Negative revenue:** Exclude it even when the year is 2021.
- **Positive revenue in another year:** It has no effect on this report.
- **Empty result:** Return the correct column with no rows when nobody qualifies.
