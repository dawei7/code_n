# Product Sales Analysis II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1069 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [product-sales-analysis-ii](https://leetcode.com/problems/product-sales-analysis-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/product-sales-analysis-ii/).

### Goal
For every product that appears in the sales table, report the total quantity sold across all its sale records.

### Query Contract
**Input table**

- `Sales(sale_id, product_id, year, quantity, price)`: Sale records for products.

**Output columns**

- `product_id`
- `total_quantity`

### Examples
**Example 1**

`Sales`

| sale_id | product_id | year | quantity | price |
|---:|---:|---:|---:|---:|
| 1 | 100 | 2008 | 10 | 5000 |
| 2 | 100 | 2009 | 12 | 5000 |
| 7 | 200 | 2011 | 15 | 9000 |

Output:

| product_id | total_quantity |
|---:|---:|
| 100 | 22 |
| 200 | 15 |

---

## Solution
### Approach
Group `Sales` by `product_id` and sum the `quantity` column for each group.

No join is required because the requested output contains only sales-table fields.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query groups all rows in `Sales`.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
