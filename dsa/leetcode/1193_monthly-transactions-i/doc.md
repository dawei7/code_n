# Monthly Transactions I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1193 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [monthly-transactions-i](https://leetcode.com/problems/monthly-transactions-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/monthly-transactions-i/).

### Goal
For each month and country, report total transactions, approved transactions, total amount, and approved amount.

### Query Contract
**Input table**

- `Transactions(id, country, state, amount, trans_date)`: Transaction records.

**Output columns**

- `month`
- `country`
- `trans_count`
- `approved_count`
- `trans_total_amount`
- `approved_total_amount`

### Examples
**Example 1**

`Transactions`

| id | country | state | amount | trans_date |
|---:|---|---|---:|---|
| 1 | US | approved | 1000 | 2018-12-18 |
| 2 | US | declined | 2000 | 2018-12-19 |
| 3 | US | approved | 2000 | 2019-01-01 |
| 4 | DE | approved | 2000 | 2019-01-07 |

Output:

| month | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
|---|---|---:|---:|---:|---:|
| 2018-12 | US | 2 | 1 | 3000 | 1000 |
| 2019-01 | US | 1 | 1 | 2000 | 2000 |
| 2019-01 | DE | 1 | 1 | 2000 | 2000 |

---

## Solution
### Approach
Group rows by `country` and the year-month prefix of `trans_date`. Use conditional aggregation to count approved rows and sum approved amounts while also computing the totals over all rows in the group.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, transactions are grouped once by month and country.
- **Space Complexity**: Depends on the execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
