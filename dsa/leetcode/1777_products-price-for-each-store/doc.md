# Product's Price for Each Store

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1777 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/products-price-for-each-store/) |

## Problem Description

### Goal

The `Products` table records prices in row form. Each row identifies a product, one of the stores `"store1"`, `"store2"`, or `"store3"`, and that product's price at the store. The pair `(product_id, store)` is unique, so a product has at most one recorded price per store.

Pivot these rows into one row per product. The result must contain `product_id` followed by columns `store1`, `store2`, and `store3`. Put each recorded price in its store's column and use `NULL` when the product is not available at that store. The rows may be returned in any order.

### Function Contract

**Input table**

- `Products(product_id, store, price)`: `store` is one of `"store1"`, `"store2"`, or `"store3"`.
- `(product_id, store)` is the primary key.
- Let $R$ be the number of input rows and $P$ the number of distinct product IDs.

**Return value**

Return one row per product with columns `product_id`, `store1`, `store2`, and `store3`.

### Examples

**Example 1**

Input:

| product_id | store | price |
|---:|---|---:|
| 0 | store1 | 95 |
| 0 | store3 | 105 |
| 0 | store2 | 100 |
| 1 | store1 | 70 |
| 1 | store3 | 80 |

Output:

| product_id | store1 | store2 | store3 |
|---:|---:|---:|---:|
| 0 | 95 | 100 | 105 |
| 1 | 70 | null | 80 |

**Example 2**

A product recorded only at `"store2"` produces `NULL`, its price, and `NULL` in the three store columns.

**Example 3**

A product with one row for every store produces a completely populated result row.
