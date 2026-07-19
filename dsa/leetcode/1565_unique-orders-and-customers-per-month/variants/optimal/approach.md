## General
**Filter before aggregating**

Apply `invoice > 20` in the `WHERE` clause. The inequality is strict: an invoice equal to `20` contributes to neither count. Filtering first also ensures that a month containing only nonqualifying orders does not create an output group.

**Use the year and month as one grouping key**

Format `order_date` as `YYYY-MM` with `DATE_FORMAT`. Including the year prevents, for example, January 2020 and January 2021 from being merged. The zero-padded representation also supplies the requested `month` value directly.

**Count rows and distinct customers separately**

Because `order_id` is unique, `COUNT(order_id)` is the number of qualifying orders in a month. Customers can place more than one order, so `COUNT(DISTINCT customer_id)` is required for `customer_count`. Grouping by the same formatted month produces exactly one row per qualifying calendar month, with both aggregates evaluated over precisely that month's filtered rows.

## Complexity detail
For $r$ order rows, filtering is linear and a portable sort-based grouping has an $O(r \log r)$ time upper bound. A database can reduce this toward linear time with hash aggregation or a suitable index, but the query does not depend on either optimization.

The filtered and grouped working data can contain $O(r)$ rows or distinct values, so the portable auxiliary-space bound is $O(r)$.

## Alternatives and edge cases
- **Extract year and month separately:** grouping by `YEAR(order_date)` and `MONTH(order_date)` is equivalent, but the formatted key is still needed for the output.
- **Correlated monthly subqueries:** derive each month and rescan `Orders` to compute its two counts. This is correct but can take $O(r^2)$ time when many months are present.
- **Conditional aggregation without filtering:** conditional counts can work, but grouping every input month can incorrectly retain a month whose qualifying counts are both zero unless it is removed afterward.
- Invoices equal to `20` are excluded because the predicate is strictly greater than `20`.
- Several orders from one customer increase `order_count` multiple times but `customer_count` once within that month.
- The same customer appearing in different months counts once in each relevant monthly group.
- The year is part of the group, so equal month numbers in different years remain separate.
- Months with no qualifying order are absent rather than reported with zero counts.
- Input row order has no effect on grouping, and the output order is unrestricted.
