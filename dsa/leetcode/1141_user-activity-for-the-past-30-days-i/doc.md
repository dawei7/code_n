# User Activity for the Past 30 Days I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1141 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [user-activity-for-the-past-30-days-i](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/).

### Goal
For each day in the 30-day window ending on `2019-07-27`, report how many distinct users were active on that day.

### Query Contract
**Input table**

- `Activity(user_id, session_id, activity_date, activity_type)`: User activity events.

**Output columns**

- `day`
- `active_users`

### Examples
**Example 1**

`Activity`

| user_id | session_id | activity_date | activity_type |
|---:|---:|---|---|
| 1 | 1 | 2019-07-20 | open_session |
| 1 | 1 | 2019-07-20 | scroll_down |
| 2 | 4 | 2019-07-20 | open_session |
| 3 | 5 | 2019-07-21 | send_message |
| 4 | 6 | 2019-06-10 | open_session |

Output:

| day | active_users |
|---|---:|
| 2019-07-20 | 2 |
| 2019-07-21 | 1 |

---

## Solution
### Approach
Filter rows to activity dates from `2019-06-28` through `2019-07-27`, inclusive. Group by `activity_date` and count distinct `user_id` values for each date.

Only dates with at least one active user appear in the output.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query filters activity rows and groups by date.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
