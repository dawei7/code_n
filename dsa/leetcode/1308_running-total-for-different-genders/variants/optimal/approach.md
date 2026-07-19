## General
**Partition the running sum by gender**

Use `SUM(score_points)` as a window aggregate. `PARTITION BY gender` starts an independent accumulation for each team, and `ORDER BY day` establishes chronological prefix order inside that partition.

Because `(gender, day)` is unique, the ordered window has one row per position. An explicit `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` frame states the intended prefix exactly: the frame for a row contains every earlier row of the same gender plus that row itself. Its sum is therefore precisely the required cumulative score.

**Separate calculation order from display order**

Window ordering determines which rows contribute to each total, but SQL does not guarantee final presentation order from a window clause alone. Add an outer `ORDER BY gender, day` so the returned relation follows the required gender-first chronological order.

## Complexity detail
The database partitions and orders $n$ rows for the window computation, which takes $O(n\log n)$ time under the standard comparison-sorting model. The ordered window operation and result materialization can use $O(n)$ space.

## Alternatives and edge cases
- **Correlated prefix subquery:** Summing all same-gender rows with `day <= current_day` for every outer row is correct, but without relying on a special index plan it performs $O(n^2)$ row comparisons.
- **Self-join and group:** Joining each row to all earlier same-gender rows and grouping produces the same totals, while also materializing a potentially quadratic intermediate relation.
- **Independent partitions:** The female and male running totals must never contribute to one another, even on the same date.
- **First date:** The earliest row for a gender has a total equal to its own `score_points`.
- **Missing dates:** Cumulative totals advance only on dates present in the table; no synthetic calendar rows are returned.
- **Input order:** Physical insertion order is irrelevant because both the window and final result use explicit date ordering.
