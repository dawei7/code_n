## General

**Count a partition without collapsing its rows**

A `GROUP BY team_id` can calculate one size per team, but the requested output has one row per employee. Use a windowed `COUNT(*)` partitioned by `team_id`. The partition makes every row with the same team identifier share one counting frame, while the window operation preserves the original employee rows.

Select `employee_id` directly and name the window count `team_size`. Each employee therefore retains its own identifier and receives the size of exactly its team. An `ORDER BY employee_id` makes local verification deterministic even though the source contract permits any output order.

**Why each count and output row is exact**

For an employee row $e$, the window partition consists of all and only rows whose `team_id` equals the team identifier on $e$. `COUNT(*)` therefore equals the cardinality of $e$'s team. A window aggregate annotates rows instead of merging them, so the primary-key row for every employee survives exactly once. The projection consequently returns every employee with the correct team size and introduces no additional rows.

## Complexity detail

A database engine can partition or sort the $n$ rows by `team_id` and order the output in $O(n \log n)$ time. The window and ordered result may require $O(n)$ working space. Physical plans can vary by engine and available indexes.

## Alternatives and edge cases

- **Aggregate then join:** Grouping by `team_id` and joining the counts back to `Employee` is also correct, but requires an additional relational step.
- **Correlated count subquery:** Counting matching team rows separately for every employee is simple but can take $O(n^2)$ time without a supporting index.
- **Self-join then group:** Joining every employee to all teammates and grouping by employee identifier is correct but can materialize a quadratic intermediate relation for one large team.
- **Plain `GROUP BY team_id`:** This produces one row per team and loses the required one-row-per-employee cardinality.
- **Empty table:** The window receives no rows and the result is empty.
- **Singleton team:** Its sole employee receives `team_size = 1`.
- **Noncontiguous identifiers:** Counts depend only on equal `team_id` values, not on numeric adjacency.
- **Signed identifiers:** Negative and zero identifiers require no special handling because partition membership uses equality only.
- **Several equal-size teams:** Each employee still receives the count from their own partition.
- **Output cardinality:** The query must return exactly one row per input employee rather than one row per team.
- **Result order:** The source permits any order; the final sort is only a deterministic local presentation choice.
