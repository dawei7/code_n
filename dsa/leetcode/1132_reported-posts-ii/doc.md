# Reported Posts II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1132 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [reported-posts-ii](https://leetcode.com/problems/reported-posts-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/reported-posts-ii/).

### Goal
For each action date with spam reports, compute the percentage of distinct reported spam posts that were later removed. Return the average of those daily percentages, rounded to two decimal places.

### Query Contract
**Input tables**

- `Actions(user_id, post_id, action_date, action, extra)`: User actions; spam reports have `action = 'report'` and `extra = 'spam'`.
- `Removals(post_id, remove_date)`: Posts that were removed.

**Output columns**

- `average_daily_percent`

### Examples
**Example 1**

`Actions`

| user_id | post_id | action_date | action | extra |
|---:|---:|---|---|---|
| 2 | 2 | 2019-07-04 | report | spam |
| 3 | 4 | 2019-07-04 | report | spam |
| 4 | 3 | 2019-07-02 | report | spam |
| 5 | 2 | 2019-07-03 | report | racism |

`Removals`

| post_id | remove_date |
|---:|---|
| 2 | 2019-07-20 |
| 3 | 2019-07-18 |

Output:

| average_daily_percent |
|---:|
| 75.00 |

---

## Solution
### Approach
Build the set of distinct spam-reported posts per `action_date`. Left join those rows to `Removals` to know which reported posts were removed. For each date, compute `removed_distinct_posts / reported_distinct_posts * 100`.

Finally average the daily percentages and round to two decimal places.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query filters reported spam rows, joins removals, groups by date, and averages.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
