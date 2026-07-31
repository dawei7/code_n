## General

**Normalize every meeting to its Monday.** The requested grouping is a Monday–Sunday calendar week, so each meeting needs a stable week key. MySQL's native query uses `YEARWEEK(meeting_date, 1)`. The app-local SQLite query subtracts the date's zero-based offset from Monday and stores the resulting Monday date as `week_start`. Using a date rather than a bare week number also keeps weeks from different years distinct.

**Reduce meetings before joining employee details.** Group `meetings` by `employee_id` and the Monday week key, sum `duration_hours`, and retain only groups whose sum is strictly greater than 20. Each remaining row now represents exactly one meeting-heavy employee-week. Meeting type does not enter the grouping or filter because every listed type contributes its full duration.

Join those reduced rows to `employees`, group by the employee identity fields, and count the retained weeks. The `HAVING COUNT(*) >= 2` condition applies after weekly aggregation, so it measures qualifying weeks rather than meetings. Every output count is exact because the first grouping creates one row per employee-week and the second grouping counts precisely those rows exceeding the threshold. Finally order the counts descending and names ascending as required.

## Complexity detail

Let $M$ be the number of meeting rows and $E$ the number of employee rows. Without assuming indexes or hash aggregation, grouping meetings can take $O(M\log M)$ comparison work. Grouping and sorting at most $E$ result groups costs $O(E\log E)$, for total time $O(M\log M+E\log E)$ and $O(M+E)$ working space. Hash aggregation or suitable indexes may reduce the practical grouping cost.

The benchmark defines $S=E$ and supplies four meetings per employee, so $M=4S$. The accepted strategy aggregates `meetings` once. A calibrated correct alternative uses correlated weekly subqueries for each employee and repeatedly scans the meeting relation, producing quadratic growth without a supporting index.

## Alternatives and edge cases

- **Correlated counting per employee:** It can express the same result, but repeated scans of `meetings` may grow quadratically with the employee count.
- **Grouping by a Sunday-based week number:** Default week functions may start weeks on Sunday, which incorrectly separates Sunday from its preceding Monday–Saturday group.
- **Grouping by week number alone:** Week numbers repeat across years; include the week-year or use the actual Monday date.
- **Exactly 20 hours:** The condition is strictly greater than 20, so equality is not meeting-heavy.
- **One heavy week:** An employee must have at least two distinct qualifying weeks, regardless of how many meetings created the one heavy total.
- **Several meetings on one date:** Sum all durations before applying the weekly threshold.
- **Meeting type:** `Team`, `Client`, and `Training` durations all count; the type does not filter rows.
- **Employees without meetings:** They produce no weekly group and cannot qualify.
- **Ordering ties:** Equal heavy-week counts are ordered by `employee_name` ascending.
