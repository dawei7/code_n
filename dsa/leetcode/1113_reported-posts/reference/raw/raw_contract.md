## Function Contract

**Input table**

- `Actions(user_id, post_id, action_date, action, extra)`: $R$ activity rows. Duplicate rows are allowed; `action` belongs to the exact six-value source domain, and `extra` contains optional action-specific information.

Filter to report actions dated `2019-07-04`. Within each `extra` value represented by those rows, count distinct `post_id` values rather than action rows or reporters.

**Return value**

- `report_reason`: the qualifying report row's `extra` value.
- `report_count`: the number of distinct posts reported for that reason yesterday.

Return one row for every represented report reason with a nonzero post count, in any order. If yesterday has no report rows, return an empty result.
