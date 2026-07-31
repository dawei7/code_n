## General

**Classify dates inside the aggregate**

Convert each `submit_date` to its day-of-week number. In the app's SQLite
adapter, `strftime('%w', ...)` returns Sunday as `0` through Saturday as `6`;
the native MySQL query uses `DAYOFWEEK`, whose weekend values are `1` and `7`.

For every row, add one to `weekend_cnt` exactly when the date is Saturday or
Sunday. A second conditional sum adds one to `working_cnt` for the remaining
five day values. These conditions are disjoint and cover the full week, so
each task contributes to exactly one count. A single aggregate without
grouping produces the required one-row result, independent of assignee IDs or
input order.

## Complexity detail

Let $r$ be the number of rows in `Tasks`. The query classifies each row once,
using $O(r)$ time. It maintains two aggregate counters and produces one output
row, so its auxiliary space is $O(1)$ in the standard streaming aggregate
model. Exact physical execution remains database-engine dependent.

## Alternatives and edge cases

- **Two filtered subqueries:** Counting weekend and weekday rows separately is correct but scans the table twice and needs extra query structure.
- **Group by day name:** This produces up to seven rows that must be pivoted or aggregated again.
- **Locale-dependent names:** Comparing formatted names such as `Saturday` can depend on language settings; numeric weekday values avoid that issue.
- **Saturday and Sunday:** Both endpoints belong to the weekend group.
- **Monday and Friday:** These are working days, as are Tuesday through Thursday.
- **Repeated assignee:** Every task row counts independently; `assignee_id` is not a grouping key.
- **Month and year boundaries:** Weekday extraction operates on the full date, so calendar boundaries require no special case.
