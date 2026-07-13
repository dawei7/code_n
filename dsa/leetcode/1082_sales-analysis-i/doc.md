# Sales Analysis I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1082 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [sales-analysis-i](https://leetcode.com/problems/sales-analysis-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sales-analysis-i/).

### Goal
Find the seller or sellers with the highest total sales amount.

### Query Contract
**Input table**

- `Sales(seller_id, product_id, buyer_id, sale_date, quantity, price)`: Sale records.

**Output columns**

- `seller_id`

### Examples
**Example 1**

`Sales`

| seller_id | product_id | buyer_id | sale_date | quantity | price |
|---:|---:|---:|---|---:|---:|
| 1 | 1 | 1 | 2019-01-21 | 2 | 2000 |
| 1 | 2 | 2 | 2019-02-17 | 1 | 800 |
| 2 | 2 | 3 | 2019-06-02 | 1 | 800 |
| 3 | 3 | 4 | 2019-05-13 | 2 | 2800 |

Output:

| seller_id |
|---:|
| 1 |
| 3 |

---

## Solution
### Approach
Group sales by `seller_id` and sum `price` for each seller. Return every seller whose sum equals the maximum seller sum.

This can be written with a grouped subquery and a `HAVING` comparison, or with a ranking window over grouped totals.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query groups all sales rows by seller.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
