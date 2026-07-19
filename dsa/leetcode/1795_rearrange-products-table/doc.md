# Rearrange Products Table

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/rearrange-products-table/) |
| Frontend ID | 1795 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

The `Products` table stores one row per product. Its primary key is `product_id`, and the nullable integer columns `store1`, `store2`, and `store3` contain that product's price in each named store. A `NULL` price means the product is unavailable at that store.

Rearrange this wide representation into rows with the columns `(product_id, store, price)`. For every non-null store price, emit one row whose `store` value is the corresponding literal name `"store1"`, `"store2"`, or `"store3"`. Do not emit unavailable product-store combinations. The result may be returned in any order.

### Function Contract

**Inputs**

- `Products`: a table with unique integer `product_id` values and nullable integer columns `store1`, `store2`, and `store3`.
- Let $R$ be the number of product rows and $K$ the number of non-null price fields, so $0 \le K \le 3R$.

**Return value**

- Return columns `product_id`, `store`, and `price`, with exactly one row for each of the $K$ available product-store combinations.
- `store` must identify the source price column, and `price` must preserve its non-null integer value.

### Examples

**Example 1**

- Input: `Products = [[0,95,100,105],[1,70,NULL,80]]`
- Output: `[[0,"store1",95],[0,"store2",100],[0,"store3",105],[1,"store1",70],[1,"store3",80]]`

Product `0` contributes three rows, while product `1` contributes none for `store2`.

**Example 2**

- Input: `Products = [[7,NULL,42,NULL]]`
- Output: `[[7,"store2",42]]`

Only the non-null second-store price becomes a result row.

**Example 3**

- Input: `Products = [[8,NULL,NULL,NULL]]`
- Output: `[]`

A product unavailable in every store contributes no rows.
