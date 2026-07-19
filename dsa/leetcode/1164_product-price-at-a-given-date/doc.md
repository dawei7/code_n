# Product Price at a Given Date

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1164 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/product-price-at-a-given-date/) |

## Problem Description

### Goal

The `Products` table records changes to product prices. Each row says that one product's price became `new_price` on `change_date`, and the combination `(product_id, change_date)` is unique. Before its first recorded change, every product has an initial price of `10`.

Find the price of every product on `2019-08-16`. For a product with one or more changes on or before that date, use the price from its latest such change, including a change made exactly on the target date. If all of a product's changes occur later, report its initial price. The result may be returned in any order.

### Function Contract

**Input table**

- `Products(product_id, new_price, change_date)`: Each row records a price change; `(product_id, change_date)` is the primary key.
- Let $r$ be the number of rows in `Products`.

**Return value**

A relation containing one row per distinct product with:

- `product_id`: The product identifier.
- `price`: Its effective price on `2019-08-16`.

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
