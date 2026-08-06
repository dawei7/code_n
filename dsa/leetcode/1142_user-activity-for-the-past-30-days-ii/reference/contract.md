## Function Contract

**Input table**

- `Activity(user_id, session_id, activity_date, activity_type)`: activity events for sessions owned by users. The table may contain duplicate rows, but a given session belongs to only one user.

Let $R$ be the number of rows in `Activity`.

The inclusive 30-day period is `2019-06-28` through `2019-07-27`. Count each qualifying `session_id` once within its owning user's group, even when that session has several qualifying events or activity types.

**Return value**

- A one-row, one-column table named `average_sessions_per_user`. Its value is the average distinct-session count across users with at least one qualifying activity, rounded to two decimal places; when there is no such user, the value is `0`.
