# Customers Who Bought All Products

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1045 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [customers-who-bought-all-products](https://leetcode.com/problems/customers-who-bought-all-products/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/customers-who-bought-all-products/).

### Goal
Given customer purchases and the catalog of products, report the customers who bought every product listed in the product table.

### Query Contract
**Input tables**

- `Customer(customer_id, product_key)`: Purchase records.
- `Product(product_key)`: Products that must all be covered.

**Output columns**

- `customer_id`: Customers who purchased every product at least once.

### Examples
**Example 1**

`Customer`

| customer_id | product_key |
|---:|---:|
| 1 | 5 |
| 2 | 6 |
| 3 | 5 |
| 3 | 6 |
| 1 | 6 |

`Product`

| product_key |
|---:|
| 5 |
| 6 |

Output:

| customer_id |
|---:|
| 1 |
| 3 |

---

## Solution
### Approach
Group purchases by `customer_id` and count each customer's distinct purchased products. A customer qualifies when that count equals the number of rows in `Product`.

The query can be written with `GROUP BY customer_id` and a `HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product)` condition.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query groups the `Customer` rows and compares each group with the product count.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
