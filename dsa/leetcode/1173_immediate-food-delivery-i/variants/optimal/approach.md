## General
**Turn the classification into a numeric contribution.** A `CASE` expression emits `1.0` when `order_date = customer_pref_delivery_date` and `0.0` otherwise. Each row therefore contributes exactly the indicator for being immediate.

**Aggregate the ratio directly.** The average of these zero-or-one indicators is the fraction of immediate orders. Multiplying that average by `100.0` converts it to a percentage, and `ROUND(..., 2)` supplies the required precision. Using decimal literals avoids accidental integer division in database engines where dividing integers would truncate.

Because the query has no `GROUP BY`, the aggregate produces exactly one output row. Aliasing the expression as `immediate_percentage` establishes the required column name.

## Complexity detail
The aggregate examines each of the $n$ delivery rows once, so its logical running time is $O(n)$. Apart from the aggregate's counters, it needs $O(1)$ working space; physical execution details remain database-engine dependent.

## Alternatives and edge cases
- **Conditional `SUM` divided by `COUNT`:** This is equally valid and has the same $O(n)$ logical cost, provided the division is forced to use a non-integer numeric type.
- **Filter and count in a subquery:** Counting immediate rows separately and dividing by another total count is correct but may require two scans instead of one.
- **All immediate orders:** The indicator average is `1`, producing `100.00`.
- **No immediate orders:** The indicator average is `0`, producing `0.00`.
- **Repeated customer:** Classification is per delivery row, not per distinct customer.
- **Scheduled boundary:** Any preferred date later than the order date is scheduled; only exact equality is immediate.
