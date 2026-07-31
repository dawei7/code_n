## General

Group the table by `order_date`, because the requested denominator is all orders placed on one particular date. Within each group, the comparison `order_date = customer_pref_delivery_date` evaluates to `1` for an immediate order and `0` for a scheduled order in MySQL.

Summing that indicator gives the number of immediate orders. Dividing by `COUNT(*)` gives their fraction of the date's orders; multiplying by `100.0` converts it to a percentage. Using a decimal multiplier prevents unintended integer arithmetic. Apply `ROUND(..., 2)` only after forming the percentage, and name the expression `immediate_percentage`.

Grouping already emits exactly one row for each unique order date. The final `ORDER BY order_date` establishes the required ascending chronological order.

## Complexity detail

Let $R$ be the number of rows in `Delivery`. A general database execution groups all $R$ rows and orders the grouped output, giving an $O(R\log R)$ upper bound and $O(R)$ working space. Database indexes and the optimizer may reduce the realized work. The benchmark uses `size` as $R$ and contrasts the grouped scan with a correlated query that recounts the same date for every source row.

## Alternatives and edge cases

- **`AVG` of the Boolean condition:** MySQL can compute `100.0 * AVG(order_date = customer_pref_delivery_date)` directly; the explicit sum and count make the numerator and denominator visible.
- **Conditional aggregation:** `SUM(CASE WHEN ... THEN 1 ELSE 0 END)` is more portable to SQL dialects without numeric Boolean expressions, but is longer.
- **Correlated recounts:** Counting a date's rows separately for every delivery repeats work and can become quadratic.
- Dates with no immediate orders must produce `0.00`, not disappear from the output.
- Dates containing only immediate orders must produce `100.00`.
- Multiply by `100.0` before rounding, and round the percentage rather than the raw fraction.
- Explicit ascending order is required even if a particular grouping plan happens to emit sorted dates.
