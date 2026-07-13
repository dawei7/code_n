# User Activity for the Past 30 Days II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1142 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [user-activity-for-the-past-30-days-ii](https://leetcode.com/problems/user-activity-for-the-past-30-days-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/user-activity-for-the-past-30-days-ii/).

### Goal
For the 30-day window ending on `2019-07-27`, compute the average number of sessions per active user. The result is rounded to two decimal places.

### Query Contract
**Input table**

- `Activity(user_id, session_id, activity_date, activity_type)`: User activity events.

**Output columns**

- `average_sessions_per_user`

### Examples
**Example 1**

`Activity`

| user_id | session_id | activity_date | activity_type |
|---:|---:|---|---|
| 1 | 1 | 2019-07-20 | open_session |
| 1 | 1 | 2019-07-20 | scroll_down |
| 1 | 2 | 2019-07-21 | open_session |
| 2 | 3 | 2019-07-21 | send_message |
| 3 | 4 | 2019-06-10 | open_session |

Output:

| average_sessions_per_user |
|---:|
| 1.50 |

---

## Solution
### Approach
Filter to dates from `2019-06-28` through `2019-07-27`, inclusive. Count distinct sessions and distinct active users in that filtered set, then divide sessions by users and round to two decimal places.

If no users are active in the window, the average should be reported as `0.00`.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query filters rows and counts distinct users and sessions.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
