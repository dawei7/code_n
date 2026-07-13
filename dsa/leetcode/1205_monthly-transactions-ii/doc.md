# Monthly Transactions II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1205 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [monthly-transactions-ii](https://leetcode.com/problems/monthly-transactions-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/monthly-transactions-ii/).

### Goal
For each month and country, report approved transaction counts and amounts together with chargeback counts and amounts. Approved transactions are counted in their transaction month; chargebacks are counted in their chargeback month.

### Query Contract
**Input tables**

- `Transactions(id, country, state, amount, trans_date)`: Transaction records.
- `Chargebacks(trans_id, trans_date)`: Chargeback events linked to transactions.

**Output columns**

- `month`
- `country`
- `approved_count`
- `approved_amount`
- `chargeback_count`
- `chargeback_amount`

### Examples
**Example 1**

`Transactions`

| id | country | state | amount | trans_date |
|---:|---|---|---:|---|
| 101 | US | approved | 1000 | 2019-05-18 |
| 102 | US | declined | 2000 | 2019-05-19 |
| 103 | US | approved | 3000 | 2019-06-10 |
| 104 | US | declined | 4000 | 2019-06-13 |
| 105 | US | approved | 5000 | 2019-06-15 |

`Chargebacks`

| trans_id | trans_date |
|---:|---|
| 102 | 2019-05-29 |
| 101 | 2019-06-30 |
| 105 | 2019-09-18 |

Output:

| month | country | approved_count | approved_amount | chargeback_count | chargeback_amount |
|---|---|---:|---:|---:|---:|
| 2019-05 | US | 1 | 1000 | 1 | 2000 |
| 2019-06 | US | 2 | 8000 | 1 | 1000 |
| 2019-09 | US | 0 | 0 | 1 | 5000 |

---

## Solution
### Approach
Create a unified event stream:

- approved transactions contribute approved count and amount in `trans_date` month
- chargebacks join back to their transaction for country and amount, then contribute chargeback count and amount in the chargeback `trans_date` month

Union those event rows and aggregate by month and country.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, approved transactions and chargebacks are unioned and grouped.
- **Space Complexity**: Depends on the execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
