## General

For a one-based minute $m$, subtracting one converts it to a zero-based position. Integer division by six identifies the zero-based block, and adding one restores the required interval number:

$$
\operatorname{interval}(m) = \left\lfloor\frac{m-1}{6}\right\rfloor + 1.
$$

This formula sends both endpoints correctly: minute `6` maps to interval `1`, while minute `7` maps to interval `2`. The native MySQL query expresses the floor division with `DIV`; the app-local SQLite query uses an integer `CAST` around the quotient.

Group rows by this derived interval and apply `SUM(order_count)`. Every minute receives exactly one interval key, so each count contributes once to the correct six-minute total. Finally, `ORDER BY interval_no` makes the required ascending order explicit rather than relying on an engine's grouping order.

## Complexity detail

Let $M$ be the number of rows and $I=M/6$ the number of intervals. Computing bucket keys and aggregate totals requires $O(M)$ expected time with hash aggregation. Ordering the $I$ result groups costs $O(I \log I)$ time, for $O(M + I \log I)$ overall, and the aggregate state uses $O(I)$ space. A database may exploit ordered access to improve the physical plan, but these bounds require no particular index plan.

## Alternatives and edge cases

- **`CEIL(minute / 6)`:** Ceiling division yields the same one-based interval numbers in MySQL, but zero-based integer division makes the boundary transformation explicit and avoids floating-point arithmetic.
- **Correlated interval totals:** Generating the distinct intervals and rescanning `Orders` for each total is correct but performs $O(MI)$ work instead of one aggregation pass.
- **Window sum plus deduplication:** A window partitioned by the interval key can compute each total, followed by one row per interval; this is valid but more elaborate than `GROUP BY`.
- **Minutes `6` and `7`:** These consecutive minutes straddle an interval boundary and must map to intervals `1` and `2`, respectively.
- **Zero orders:** Rows with `order_count = 0` remain part of their interval and do not suppress a zero total.
- **Output ordering:** SQL does not guarantee grouped-row order, so the final ascending `ORDER BY` is required.
