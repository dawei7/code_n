## General

**Filter to the exact inclusive 30-day window**

The reporting date is `2019-07-27`, and that date is included. A 30-day inclusive period contains the reporting date itself plus the preceding 29 dates, so the earliest accepted date is `2019-06-28`.

The query expresses this with two conditions:

`activity_date <= '2019-07-27'`

and

`DATEDIFF('2019-07-27', activity_date) < 30`.

In MySQL, `DATEDIFF(later, earlier)` returns the number of date boundaries between its arguments. On `2019-07-27` the difference is zero; on `2019-06-28` it is 29. Both satisfy the strict less-than-30 test. On `2019-06-27` the difference is 30, so it is excluded.

The upper-bound comparison is still necessary. A date after `2019-07-27` would produce a negative `DATEDIFF` result, and a negative number is also less than 30. Without the explicit `activity_date <= '2019-07-27'` condition, future activities could incorrectly enter the result. Together, the predicates implement exactly the closed date interval from `2019-06-28` through `2019-07-27`.

**Group activities by calendar day**

After filtering, the requested output has one row per date that has qualifying activity. `GROUP BY 1` groups by the first expression in the select list, which is `activity_date AS day`. It is a positional shorthand for grouping by `activity_date`.

SQL grouping naturally omits dates for which no source row survives the filter. This matches the example's statement that days with zero active users do not need output rows. Generating a calendar table and left joining it would instead create zero-count days, which is outside the requested result shape.

The alias `day` gives the output column its required name. Since the result may be returned in any order, no `ORDER BY` clause is necessary. Omitting ordering also avoids promising a presentation order that the contract does not require.

**Count users, not activity rows**

A user is active on a day when that user performs at least one activity on that date. One user can have many activity rows on the same date: a session might be opened, scrolled, used to send a message, and ended. The table may even contain duplicate rows. Counting raw rows would therefore measure activity events rather than active users.

`COUNT(DISTINCT user_id)` deduplicates all appearances of the same user inside each date group. Whether a user has one qualifying row, several activity types, several sessions, or duplicate copies of the same row, that user contributes exactly one to that day's count.

The query deliberately does not filter on `activity_type`. The statement says every listed activity type counts as valid activity. Once a row falls in the date window, its presence is enough to make its user active on that day. Adding a condition for only session-opening events, messages, or any other subset would undercount legitimate active users.

The `session_id` column is also irrelevant for this report. Sessions matter only as the source of activities; the measurement unit is a distinct user-date pair. The guarantee that each session belongs to exactly one user is consistent with the data model but requires no special join or grouping here.

**Follow the query's logical flow**

Conceptually, SQL evaluates this solution in three useful stages:

1. `FROM Activity` begins with the activity-event rows.
2. `WHERE` keeps only rows in the required date window.
3. `GROUP BY` partitions those rows by date, and `COUNT(DISTINCT user_id)` produces one count per partition.

The `SELECT` projection names the grouped date `day` and the distinct count `active_users`.

In the example, all rows dated `2019-06-25` are filtered out. On `2019-07-20`, user one appears three times and user two appears once, but the distinct user set is only `{1, 2}`, producing two. On `2019-07-21`, users two and three each appear multiple times, but the distinct set again has size two.

**Why the result is correct**

For every returned row, the date predicates prove its day belongs to the required interval. Grouping ensures all and only qualifying rows for that one date are considered together. Distinct counting establishes a one-to-one correspondence between counted items and users who have at least one qualifying activity on that date. Thus `active_users` is exactly the daily active-user count.

Conversely, any user active on a report-window date has at least one corresponding row. That row survives the filter, enters its date's group, and causes the user's identifier to appear in the distinct set. Therefore, no qualifying user is omitted. Dates without such rows form no group and are correctly absent.

## Complexity detail

Let `R` be the number of rows in `Activity`. The database must inspect candidate rows to apply the date filter. Grouping by date and computing distinct user identifiers may be implemented with sorting or hashing. Under the repository's conservative sort-based bound, the time complexity is `O(R log R)`.

The intermediate grouping and distinct sets may retain up to `O(R)` values in the worst case, so the documented space complexity is `O(R)`. A database with a suitable index or hash aggregation may perform better in practice, but physical execution depends on the optimizer, indexes, statistics, and engine. The stated bounds safely describe a general execution without relying on a particular index.

The result itself has at most 30 groups because the date interval contains only 30 days, but deduplicating users within those groups can still involve a number of identifiers proportional to `R`.

## Alternatives and edge cases

- **Count all rows per day:** `COUNT(*)` overcounts users who perform multiple activities or whose rows are duplicated. The required unit is a distinct `user_id` within each day.
- **Count distinct sessions:** `COUNT(DISTINCT session_id)` answers a different question. One user may own multiple sessions yet should contribute only one active user for a date.
- **Use only the `DATEDIFF` predicate:** Future dates yield negative differences and would incorrectly satisfy `< 30`. The explicit upper date bound prevents that leak.
- **Use `DATEDIFF <= 30`:** That includes 31 calendar dates because differences zero through 30 are all accepted. The correct inclusive 30-day window uses differences zero through 29.
- **Use a half-open interval:** `activity_date >= '2019-06-28' AND activity_date < '2019-07-28'` is an equivalent clear formulation for date values. The exact solution instead combines an upper bound with `DATEDIFF`.
- **Duplicate activity rows:** Distinct user counting makes them harmless for the active-user total.
- **Several sessions for one user on one day:** The user still contributes one because deduplication is on `user_id`, not `session_id`.
- **Any listed activity type:** Opening, ending, scrolling, and messaging all count. No type-specific predicate should be added.
- **No qualifying activity at all:** No groups are formed, so the query returns an empty result table, which is consistent with omitting zero-activity days.
- **Boundary dates:** Activities on `2019-06-28` and `2019-07-27` are included; activities on `2019-06-27` and `2019-07-28` are excluded.
- **Output ordering:** The contract permits any order. If a consumer later requires chronological output, an `ORDER BY day` could be added, but it is unnecessary here.
