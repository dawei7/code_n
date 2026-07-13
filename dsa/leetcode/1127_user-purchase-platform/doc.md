# User Purchase Platform

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1127 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [user-purchase-platform](https://leetcode.com/problems/user-purchase-platform/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/user-purchase-platform/).

### Goal
For each spend date, report purchase totals for three platform categories: users who spent only on mobile, users who spent only on desktop, and users who spent on both. Each date should include all three platform rows, using zero totals when no users match a category.

### Query Contract
**Input table**

- `Spending(user_id, spend_date, platform, amount)`: User spending records, where `platform` is `mobile` or `desktop`.

**Output columns**

- `spend_date`
- `platform`: one of `mobile`, `desktop`, or `both`
- `total_amount`
- `total_users`

### Examples
**Example 1**

`Spending`

| user_id | spend_date | platform | amount |
|---:|---|---|---:|
| 1 | 2019-07-01 | mobile | 100 |
| 1 | 2019-07-01 | desktop | 100 |
| 2 | 2019-07-01 | mobile | 100 |
| 2 | 2019-07-02 | mobile | 100 |
| 3 | 2019-07-01 | desktop | 100 |
| 3 | 2019-07-02 | desktop | 100 |

Output:

| spend_date | platform | total_amount | total_users |
|---|---|---:|---:|
| 2019-07-01 | desktop | 100 | 1 |
| 2019-07-01 | mobile | 100 | 1 |
| 2019-07-01 | both | 200 | 1 |
| 2019-07-02 | desktop | 100 | 1 |
| 2019-07-02 | mobile | 100 | 1 |
| 2019-07-02 | both | 0 | 0 |

---

## Solution
### Approach
First aggregate spending per `(user_id, spend_date)` into mobile amount and desktop amount. Classify each user-day as `mobile`, `desktop`, or `both` based on which amounts are positive.

Then aggregate by `(spend_date, platform)`. To include zero rows, cross join all distinct spend dates with the three platform labels and left join the computed aggregates.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query performs user-day aggregation and then date-platform aggregation.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
