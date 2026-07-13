# Product Sales Analysis III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1070 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [product-sales-analysis-iii](https://leetcode.com/problems/product-sales-analysis-iii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/product-sales-analysis-iii/).

### Goal
For each product, report the sale record or records from that product's first sale year. If a product has multiple sales in its earliest year, include all of them.

### Query Contract
**Input table**

- `Sales(sale_id, product_id, year, quantity, price)`: Sale records for products.

**Output columns**

- `product_id`
- `first_year`
- `quantity`
- `price`

### Examples
**Example 1**

`Sales`

| sale_id | product_id | year | quantity | price |
|---:|---:|---:|---:|---:|
| 1 | 100 | 2008 | 10 | 5000 |
| 2 | 100 | 2009 | 12 | 5000 |
| 7 | 200 | 2011 | 15 | 9000 |

Output:

| product_id | first_year | quantity | price |
|---:|---:|---:|---:|
| 100 | 2008 | 10 | 5000 |
| 200 | 2011 | 15 | 9000 |

---

## Solution
### Approach
Find the minimum `year` for each `product_id`, then join or filter the original `Sales` rows to keep records whose year equals that product's minimum year.

This preserves duplicate first-year rows when they exist.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query computes one grouped minimum and filters sales rows against it.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
