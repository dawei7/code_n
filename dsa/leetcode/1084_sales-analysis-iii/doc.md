# Sales Analysis III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1084 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [sales-analysis-iii](https://leetcode.com/problems/sales-analysis-iii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sales-analysis-iii/).

### Goal
Report products that were sold only during the first quarter of 2019, from `2019-01-01` through `2019-03-31` inclusive. A qualifying product must have at least one sale in that period and no sales outside that period.

### Query Contract
**Input tables**

- `Product(product_id, product_name, unit_price)`: Product metadata.
- `Sales(seller_id, product_id, buyer_id, sale_date, quantity, price)`: Sale records.

**Output columns**

- `product_id`
- `product_name`

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
| 2 | 2 | 3 | 2019-06-02 | 1 | 800 |
| 3 | 3 | 4 | 2019-05-13 | 2 | 2800 |

Output:

| product_id | product_name |
|---:|---|
| 1 | S8 |

---

## Solution
### Approach
Group sales by product and use conditional aggregation. A product qualifies when every sale date is inside the first quarter window. Joining to `Product` provides the product name for the output.

One common shape is `GROUP BY product_id, product_name` with `HAVING MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31'`.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query joins product and sales rows and groups by product.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
