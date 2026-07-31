## General

**Keep observations separated by user**

Partition every window calculation by `user_id` and order each partition by `steps_date`. The rolling average over the current row and its two preceding rows then considers the only three observations that could form the required period. `LAG(steps_date, 2)` retrieves the earliest date from that same three-row window.

**Distinguish calendar days from table rows**

Three adjacent rows are not necessarily three consecutive dates. Retain a candidate only when the current date is exactly two calendar days after the date returned by `LAG`. Because `(user_id, steps_date)` is unique and the window contains exactly three rows, fitting those rows into that inclusive three-day span proves that all three dates are consecutive. The first two observations in each partition have no second predecessor and are therefore excluded automatically.

Compute `AVG(steps_count)` over the same three-row frame and round it to two decimal places. The outer query filters incomplete windows, selects the required three columns, and applies the mandated ascending order.

The native MySQL artifact expresses the same calendar window directly with `RANGE BETWEEN INTERVAL 2 DAY PRECEDING AND CURRENT ROW` and verifies completeness with a windowed `COUNT(*)`. The app-local SQL uses `ROWS`, `LAG`, and `julianday` so the repository's SQLite-based judge preserves the identical contract.

## Complexity detail

Let $S$ be the number of rows in `Steps`. Ordering the rows within user partitions costs $O(S \log S)$ time in the general case. Once ordered, the fixed-width window calculations and filtering take $O(S)$ additional time. The sort and window executor can require $O(S)$ auxiliary space.

The benchmark uses $S$ as `size` and places all rows in one consecutive-date user partition. The window solution sorts once and advances through that order. A correct correlated solution rescans the table to count and average the three-day range for each ending row, creating $O(S^2)$ work without a supporting index; it completes the workloads but fails the scaling verdict.

## Alternatives and edge cases

- **Calendar-range window:** MySQL can use a two-day `RANGE` frame and a windowed count directly. This is concise and is the remotely accepted native form, but its interval syntax is dialect-specific.
- **Three-way self join:** Join each ending row to rows exactly one and two days earlier for the same user. This is correct and clear, though performance depends heavily on primary-key lookup planning.
- **Correlated range aggregates:** Count and average matching rows in a date range for every candidate ending row. It is correct but can perform quadratic work without an index.
- **Missing middle date:** Three nearby observations must not qualify unless their dates are consecutive.
- **User boundaries:** Dates from different users can never complete one another's windows.
- **Long streaks:** Every date from the third day onward produces its own overlapping three-day average.
- **Rounding:** Apply rounding to the average, not to individual step counts, and expose the alias `rolling_average`.
- **Output order:** Sort first by `user_id`, then by `steps_date`, both ascending.
