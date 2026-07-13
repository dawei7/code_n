# Sales Analysis II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1083 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [sales-analysis-ii](https://leetcode.com/problems/sales-analysis-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sales-analysis-ii/).

### Goal
Report buyers who bought product `S8` but did not buy product `iPhone`.

### Query Contract
**Input tables**

- `Sales(seller_id, product_id, buyer_id, sale_date, quantity, price)`: Sale records.
- `Product(product_id, product_name, unit_price)`: Product metadata.

**Output columns**

- `buyer_id`

### Examples
**Example 1**

`Product`

| product_id | product_name | unit_price |
|---:|---|---:|
| 1 | S8 | 1000 |
| 2 | G4 | 800 |
| 3 | iPhone | 1400 |

`Sales`

| seller_id | product_id | buyer_id | sale_date | quantity | price |
|---:|---:|---:|---|---:|---:|
| 1 | 1 | 1 | 2019-01-21 | 2 | 2000 |
| 1 | 2 | 2 | 2019-02-17 | 1 | 800 |
| 2 | 1 | 3 | 2019-06-02 | 1 | 800 |
| 3 | 3 | 3 | 2019-05-13 | 2 | 2800 |

Output:

| buyer_id |
|---:|
| 1 |

---

## Solution
### Approach
Join `Sales` to `Product` so purchases can be filtered by product name. Group by `buyer_id`, then require that the buyer has at least one `S8` purchase and no `iPhone` purchase.

This can be expressed with conditional aggregation in `HAVING`, or with set operations that subtract iPhone buyers from S8 buyers.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query joins sales to product rows and groups or filters buyer ids.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
