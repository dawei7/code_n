## Function Contract

**Input table**

- `Traffic(user_id, activity, activity_date)`: $N$ website-activity rows for $U$ distinct users. Duplicate rows are allowed, and `activity` belongs to the exact source-defined set `login`, `logout`, `jobs`, `groups`, and `homepage`.

For each user who has at least one login, first determine the minimum `activity_date` over that user's complete login history. A first-login date qualifies when its difference from `2019-06-30` is between 0 and 90 days, inclusive. Thus the closed reporting interval is `2019-04-01` through `2019-06-30`; a future date does not qualify.

**Return value**

- `login_date`: a qualifying first-login date.
- `user_count`: the number of distinct users whose first login occurred on that date.

Return one row for each qualifying date that has at least one new user. Dates with a zero count are omitted, and result order is unrestricted. If no user's first login qualifies, return an empty result.
