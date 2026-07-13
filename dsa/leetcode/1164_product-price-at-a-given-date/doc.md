# Product Price at a Given Date

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1164 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [product-price-at-a-given-date](https://leetcode.com/problems/product-price-at-a-given-date/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/product-price-at-a-given-date/).

### Goal
For each product, report its price on `2019-08-16`. Every product has default price `10` before any recorded price changes.

### Query Contract
**Input table**

- `Products(product_id, new_price, change_date)`: Price changes for products.

**Output columns**

- `product_id`
- `price`

### Examples
**Example 1**

`Products`

| product_id | new_price | change_date |
|---:|---:|---|
| 1 | 20 | 2019-08-14 |
| 2 | 50 | 2019-08-14 |
| 1 | 30 | 2019-08-15 |
| 1 | 35 | 2019-08-16 |
| 2 | 65 | 2019-08-17 |
| 3 | 20 | 2019-08-18 |

Output:

| product_id | price |
|---:|---:|
| 1 | 35 |
| 2 | 50 |
| 3 | 10 |

---

## Solution
### Approach
For each product, find the latest change whose `change_date` is not after `2019-08-16`. Use that price when it exists; otherwise return the default price `10`.

This can be written with a window rank over eligible changes, a grouped max date joined back to the table, or a correlated subquery depending on SQL dialect preferences.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, product changes are searched up to the target date.
- **Space Complexity**: Depends on the execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
