# Product Sales Analysis I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1068 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [product-sales-analysis-i](https://leetcode.com/problems/product-sales-analysis-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/product-sales-analysis-i/).

### Goal
For each sale, report the product name together with the sale year and price.

### Query Contract
**Input tables**

- `Sales(sale_id, product_id, year, quantity, price)`: Sales records.
- `Product(product_id, product_name)`: Product metadata.

**Output columns**

- `product_name`
- `year`
- `price`

### Examples
**Example 1**

`Sales`

| sale_id | product_id | year | quantity | price |
|---:|---:|---:|---:|---:|
| 1 | 100 | 2008 | 10 | 5000 |
| 2 | 100 | 2009 | 12 | 5000 |
| 7 | 200 | 2011 | 15 | 9000 |

`Product`

| product_id | product_name |
|---:|---|
| 100 | Nokia |
| 200 | Apple |
| 300 | Samsung |

Output:

| product_name | year | price |
|---|---:|---:|
| Nokia | 2008 | 5000 |
| Nokia | 2009 | 5000 |
| Apple | 2011 | 9000 |

---

## Solution
### Approach
Join `Sales` with `Product` on `product_id`, then project only `product_name`, `year`, and `price`.

No aggregation is needed because the output keeps one row per sale record.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query scans or indexes into sales and product rows needed for the join.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
