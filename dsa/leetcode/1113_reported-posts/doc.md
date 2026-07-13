# Reported Posts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1113 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [reported-posts](https://leetcode.com/problems/reported-posts/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/reported-posts/).

### Goal
For the date `2019-07-04`, report how many distinct posts were reported for each reason.

### Query Contract
**Input table**

- `Actions(user_id, post_id, action_date, action, extra)`: User actions; for report actions, `extra` stores the report reason.

**Output columns**

- `report_reason`
- `report_count`

### Examples
**Example 1**

`Actions`

| user_id | post_id | action_date | action | extra |
|---:|---:|---|---|---|
| 1 | 1 | 2019-07-04 | view | null |
| 1 | 1 | 2019-07-04 | report | spam |
| 2 | 2 | 2019-07-04 | report | spam |
| 3 | 2 | 2019-07-04 | report | spam |
| 4 | 3 | 2019-07-04 | report | abuse |

Output:

| report_reason | report_count |
|---|---:|
| abuse | 1 |
| spam | 2 |

---

## Solution
### Approach
Filter rows to `action_date = '2019-07-04'` and `action = 'report'`. Group by the reason stored in `extra`, and count distinct `post_id` values for each reason.

Counting distinct posts avoids double-counting the same post when multiple users report it for the same reason.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query filters actions and groups reported posts by reason.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
