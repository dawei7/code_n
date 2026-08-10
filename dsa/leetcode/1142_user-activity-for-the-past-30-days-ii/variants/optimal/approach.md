## General

**Separate the calculation into per-user counts and one overall average**

The requested average is not the number of activity rows divided by the number of users. Each participating user first needs an individual count of distinct sessions with at least one activity in the reporting window. Only then are those per-user session counts averaged.

The common table expression `T` performs the first level. It groups filtered activity rows by `user_id` and produces one column:

`COUNT(DISTINCT session_id) AS sessions`.

The outer query performs the second level by applying `AVG(sessions)` to the rows of `T`. This two-stage structure matches the mathematical definition of an average across users. Trying to place `AVG(COUNT(...))` in one ordinary grouping level is not valid SQL aggregation and would blur the two different populations.

**Filter to exactly 30 inclusive dates**

The target period ends on `2019-07-27` and includes that date. Its earliest date is `2019-06-28`. The CTE uses

`activity_date <= '2019-07-27'`

together with

`DATEDIFF('2019-07-27', activity_date) < 30`.

For dates from `2019-06-28` through `2019-07-27`, the difference ranges from 29 down to zero, so the rows are retained. `2019-06-27` has difference 30 and is excluded.

The upper bound is not redundant. A future date would create a negative date difference, and that value would satisfy `< 30`. Requiring the activity date to be no later than the reporting date prevents future rows from entering the window.

**Count a session once for its user**

A session qualifies when it has at least one activity in the period. It may have several qualifying rows because the user can open it, scroll, send messages, and end it, possibly with duplicate rows in the table. `COUNT(DISTINCT session_id)` collapses all of those rows to one session inside the user's group.

The grouping is by `user_id` because the final population consists of users. The contract guarantees that each session belongs to exactly one user, so the same session identifier cannot legitimately contribute to multiple owners. Even so, the distinct count occurs within each user group, making the intended ownership boundary explicit.

There is no `activity_type` condition because every activity type listed by the schema is valid evidence that a session was active. There is also no need for a session to start or end within the period. One qualifying activity of any type is enough for that session to count.

Only users with at least one qualifying activity produce a group in `T`. This is exactly the population described by the problem: the average is across users whose sessions have activity in the window. Users with no qualifying row are absent rather than treated as having zero sessions. Including inactive users with zeros would require another user table and would change the requested denominator.

**Average, round, and handle an empty population**

For the example, `T` contains the values one for user one, one for user two, and two for user three. The outer average is therefore `(1 + 1 + 2) / 3`, which rounds to `1.33`.

`ROUND(AVG(sessions), 2)` performs the required rounding to two decimal places. Rounding must occur after the average. Rounding individual integer session counts would do nothing here, but in general the calculation's requested value is the final mean.

If no row survives the date filter, `T` is empty. An aggregate query without an outer `GROUP BY` still returns one row, but `AVG` over an empty input is `NULL`. The contract requires zero in that situation. `COALESCE(..., 0)` replaces only that null result with zero and preserves every real average.

The selected alias `average_sessions_per_user` gives the single output column its exact required name. No ordering is meaningful because the result has exactly one row.

**Why the query is correct**

Every row entering `T` is inside the required date range. For a fixed user, the distinct session aggregation counts a session if and only if at least one row for that session survived the filter. Thus each `sessions` value is exactly that user's qualifying-session count.

Every user with qualifying activity forms one group, while every user without qualifying activity forms none. Therefore, `AVG(sessions)` sums precisely the desired per-user counts and divides by precisely the number of participating users. Rounding supplies the required presentation, and the null replacement handles the only case in which that participating-user set is empty.

The two aggregation levels are both necessary. Deduplicating sessions alone provides counts but not the cross-user mean; averaging raw activity rows would overweight sessions with more events. The CTE preserves the correct unit at each level.

## Complexity detail

Let `R` be the number of rows in `Activity`. Filtering examines candidate activity rows. Grouping by user and deduplicating session identifiers can be implemented through sorting, giving the repository's conservative `O(R log R)` time bound. The final average visits at most one CTE row per participating user and is no larger than the grouping work.

The grouping and distinct-session state can contain information proportional to the number of qualifying rows, so the documented auxiliary space is `O(R)`. Physical SQL performance depends on indexes and the database optimizer; an index over dates and grouping columns or hash aggregation may reduce actual work, but the approach does not require such an assumption.

The final result is constant-sized, but the intermediate CTE and the internal distinct aggregation account for the linear space bound.

## Alternatives and edge cases

- **Average raw activity counts:** This overweights sessions that generate many events and does not compute sessions per user.
- **Count sessions without `DISTINCT`:** A session with several activity rows would be counted repeatedly. Distinct session identifiers implement the phrase “at least one activity.”
- **Average globally distinct sessions divided by users:** Because sessions belong to one user, that quotient can match some datasets, but the grouped CTE directly preserves the required per-user definition and safely exposes each user's count.
- **Include inactive users as zeros:** The input contains activity rows rather than a complete user roster, and the requested average concerns users with qualifying activity. Adding zero-session users would change the denominator.
- **Filter by `activity_type`:** Every listed activity type qualifies, so any restriction to openings, endings, scrolling, or messages would omit valid sessions.
- **Only a `DATEDIFF < 30` condition:** Future activity dates produce negative differences and would be incorrectly accepted. The upper bound closes that hole.
- **A session spans the window boundary:** It counts if at least one of its activity rows lies inside the period, regardless of when it began or ended.
- **Duplicate rows:** `COUNT(DISTINCT session_id)` prevents them from inflating a user's session total.
- **No qualifying rows:** The CTE is empty, `AVG` is null, and `COALESCE` returns the required zero.
- **Exactly one active user:** The average equals that user's distinct-session count, rounded to two decimals by the same expression.
- **Boundary dates:** `2019-06-28` and `2019-07-27` are accepted; the immediately adjacent outside dates are rejected.
- **Rounding:** The query rounds the final average rather than truncating it, preserving standard MySQL rounding behavior to two decimal places.
