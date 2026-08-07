## Description

Table: `Traffic`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| activity      | enum    |
| activity_date | date    |
+---------------+---------+
This table may have duplicate rows.
The activity column is an ENUM (category) type of ('login', 'logout', 'jobs', 'groups', 'homepage').
```

Write a solution to reports for every date within at most `90` days from today, the number of users that logged in for the first time on that date. Assume today is `2019-06-30`.

Return the result table in **any order**.

The result format is in the following example.
### Function Contract

**Input table**

- `Traffic(user_id, activity, activity_date)`: $N$ website-activity rows for $U$ distinct users. Duplicate rows are allowed, and `activity` belongs to the exact source-defined set `login`, `logout`, `jobs`, `groups`, and `homepage`.

For each user who has at least one login, first determine the minimum `activity_date` over that user's complete login history. A first-login date qualifies when its difference from `2019-06-30` is between 0 and 90 days, inclusive. Thus the closed reporting interval is `2019-04-01` through `2019-06-30`; a future date does not qualify.

**Return value**

- `login_date`: a qualifying first-login date.
- `user_count`: the number of distinct users whose first login occurred on that date.

Return one row for each qualifying date that has at least one new user. Dates with a zero count are omitted, and result order is unrestricted. If no user's first login qualifies, return an empty result.

### Examples
#### Example 1

```
**Input:**
Traffic table:
+---------+----------+---------------+
| user_id | activity | activity_date |
+---------+----------+---------------+
| 1       | login    | 2019-05-01    |
| 1       | homepage | 2019-05-01    |
| 1       | logout   | 2019-05-01    |
| 2       | login    | 2019-06-21    |
| 2       | logout   | 2019-06-21    |
| 3       | login    | 2019-01-01    |
| 3       | jobs     | 2019-01-01    |
| 3       | logout   | 2019-01-01    |
| 4       | login    | 2019-06-21    |
| 4       | groups   | 2019-06-21    |
| 4       | logout   | 2019-06-21    |
| 5       | login    | 2019-03-01    |
| 5       | logout   | 2019-03-01    |
| 5       | login    | 2019-06-21    |
| 5       | logout   | 2019-06-21    |
+---------+----------+---------------+
**Output:**
+------------+-------------+
| login_date | user_count  |
+------------+-------------+
| 2019-05-01 | 1           |
| 2019-06-21 | 2           |
+------------+-------------+
**Explanation:**
Note that we only care about dates with non zero user count.
The user with id 5 first logged in on 2019-03-01 so he's not counted on 2019-06-21.
```