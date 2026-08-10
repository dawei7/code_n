## General

**Aggregate the two relevant subscription stages separately per user.** The first common table expression, `T`, reads `UserActivity` rows whose type is not `cancelled`. That leaves `free_trial` and `paid` activity, the only stages contributing to requested averages.

It groups by both `user_id` and `activity_type`. Therefore, one user can produce up to two aggregate rows: one trial row and one paid row.

The calculated expression is

`ROUND(SUM(activity_duration) / COUNT(1), 2)`.

`SUM` adds all recorded daily minutes in that user's stage, and `COUNT(1)` counts those activity rows. Their quotient is the average activity duration across recorded days for that stage. `ROUND(..., 2)` applies the required two-decimal rounding.

Using the activity rows as days is valid because the schema's composite unique key permits at most one row for a user, date, and activity type.

**Cancelled rows neither affect averages nor disqualify a prior conversion.** A cancellation duration is not part of trial or paid activity, so filtering it before aggregation prevents its zero from lowering an average.

The request asks for users who converted from trial to paid. A user such as user four may later cancel but still had a paid stage and remains a converter. The query correctly does not exclude users merely because a cancelled row exists.

**Give the two stage aggregates meaningful column names.** CTE `F` selects only `activity_type = 'free_trial'` and renames `duration` to `trial_avg_duration`. CTE `P` selects only paid rows and renames it to `paid_avg_duration`.

These CTEs contain at most one row per user because `T` already grouped by user and type.

**Use an inner join to identify conversion.** The final query joins `F` and `P` with `USING (user_id)`. An inner join retains a user only when both a trial aggregate and a paid aggregate exist.

A trial-only user has no row in `P` and disappears, which excludes user two in the example. A paid-only user would similarly lack `F`. A user with both stages appears once with both rounded averages.

This is a concise relational definition of conversion based on the labeled activity data: membership in both stage sets.

**Order by the requested identifier.** `ORDER BY 1` refers to the first selected column, `user_id`. Ascending order is SQL's default, so converter rows appear in increasing user ID.

For user one, trial sum $45+30+60=135$ divided by three gives $45.00$. Paid sum $75+90+65=230$ divided by three gives $76.666\ldots$, rounded to $76.67$. The join places those values on one row.

For user four, two trial rows average to $37.50$ and the single paid row averages to $45.00$. The later cancelled row was removed before aggregation and does not prevent the join.

**Why the query is correct.** CTE `T` computes exactly one rounded average for every observed user-stage pair among trial and paid records. `F` and `P` partition those aggregates into the requested output roles. Their inner join returns exactly users present in both stages and combines the correct averages. The final ordering satisfies the specified presentation.

The source does not explicitly compare activity dates or enforce a seven-calendar-day window. It relies on `activity_type` labels to define which rows belong to the trial and paid periods, exactly as the provided data model and examples do. If an application allowed mislabeled chronology, additional date logic would be needed, but it is not present in this protected solution.

## Complexity detail

Let $A$ be the number of activity rows and $U$ the number of users. Filtering scans $A$ rows. Grouping by user and activity type can be implemented with hashing in expected $O(A)$ time or sorting in $O(A\log A)$ time. The manifest uses the conservative $O(A\log A)$ bound.

The two small CTE filters and their join process at most two aggregate rows per user, costing $O(U)$ expected with hash/indexed join strategies. Ordering up to $U$ converter rows costs $O(U\log U)$ and is covered by $O(A\log A)$ because $U\le A$.

Aggregate and join workspace is $O(U)$ at the logical level, matching the manifest. Exact materialization and sort memory depend on MySQL's execution plan.

## Alternatives and edge cases

- **Conditional aggregation in one grouped query:** `AVG(CASE WHEN ... END)` plus a `HAVING` condition can produce the same result without separate `F` and `P` CTEs.
- **Include cancelled rows in one average:** Their duration belongs to neither requested stage and would corrupt the result.
- **Exclude anyone who ever cancelled:** A user may convert, later cancel, and still belong in the analysis, as user four demonstrates.
- **Trial-only user:** They have no paid CTE row and are removed by the inner join.
- **Paid-only user:** They have no trial CTE row and are also excluded.
- **One activity day in a stage:** Sum divided by one returns that day's duration.
- **Several dates:** Every labeled activity row contributes equally to the daily average.
- **Round inputs before averaging:** Rounding belongs after division; durations are integers, and the source rounds only the final average.
- **Chronology:** The source infers conversion from presence of both labels and does not verify that paid dates follow trial dates.
- **Seven-day wording:** No date-range filter appears; stage membership comes from `activity_type`.
- **Later cancellation:** Filtering cancellation affects neither conversion presence nor paid average.
- **`ORDER BY 1`:** It is correct while `user_id` remains the first selected expression; naming the column directly can be clearer for maintenance.
