# New Users Daily Count

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1107 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/new-users-daily-count/) |

## Problem Description

### Goal

The `Traffic` table records users' activity on a website. Each row identifies a user, one activity from `login`, `logout`, `jobs`, `groups`, or `homepage`, and the date on which that activity occurred. A user may have several activities and may log in on more than one date.

For every date in the period of 90 days ending on `2019-06-30`, report how many users logged in for the first time on that date. A user is new only on the date of that user's earliest `login` row across the entire table: an earlier login outside the reporting period must not be discarded before finding the minimum. Return `login_date` and `user_count`; the platform allows the result rows in any order.

### Function Contract

**Inputs**

- `Traffic(user_id, activity, activity_date)`: $N$ website-activity rows concerning $U$ distinct users. The `activity` value is one of `login`, `logout`, `jobs`, `groups`, or `homepage`.

**Return value**

- One row `login_date, user_count` for each first-login date from `2019-04-01` through `2019-06-30`, inclusive.
- `user_count` is the number of users whose earliest `login` occurred on that date. Dates with no new users do not appear.
- Result order is unrestricted; the local reference orders `login_date` ascending for deterministic validation.

### Examples

**Example 1**

`Traffic`

| user_id | activity | activity_date |
|---:|---|---|
| 1 | login | 2019-05-01 |
| 1 | homepage | 2019-05-01 |
| 1 | logout | 2019-05-01 |
| 2 | login | 2019-06-21 |
| 2 | logout | 2019-06-21 |
| 3 | login | 2019-01-01 |
| 3 | jobs | 2019-01-01 |
| 3 | logout | 2019-01-01 |
| 4 | login | 2019-06-21 |
| 4 | groups | 2019-06-21 |
| 4 | logout | 2019-06-21 |
| 5 | login | 2019-03-01 |
| 5 | logout | 2019-03-01 |
| 5 | login | 2019-06-21 |
| 5 | logout | 2019-06-21 |

Output:

| login_date | user_count |
|---|---:|
| 2019-05-01 | 1 |
| 2019-06-21 | 2 |

Users `1`, `2`, and `4` have their first login inside the reporting period. User `3` first logged in too early, and user `5` is not new on June 21 because that user already logged in during March.
