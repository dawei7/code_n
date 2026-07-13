# New Users Daily Count

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1107 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [new-users-daily-count](https://leetcode.com/problems/new-users-daily-count/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/new-users-daily-count/).

### Goal
For each date in the 90-day window ending on `2019-06-30`, report how many users logged in for the first time on that date.

### Query Contract
**Input table**

- `Traffic(user_id, activity, activity_date)`: User activity records.

**Output columns**

- `login_date`
- `user_count`

### Examples
**Example 1**

`Traffic`

| user_id | activity | activity_date |
|---:|---|---|
| 1 | login | 2019-05-01 |
| 1 | homepage | 2019-05-01 |
| 2 | login | 2019-06-21 |
| 3 | login | 2019-06-21 |
| 2 | login | 2019-06-22 |
| 4 | login | 2019-03-01 |

Output:

| login_date | user_count |
|---|---:|
| 2019-05-01 | 1 |
| 2019-06-21 | 2 |

---

## Solution
### Approach
Filter to `activity = 'login'`, then find each user's first login date with `MIN(activity_date)`. Keep first-login dates between `2019-04-01` and `2019-06-30`, then group by that date and count users.

The key is to filter the 90-day window after finding each user's first login, not before.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query filters login rows, groups by user, then groups first-login dates.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
