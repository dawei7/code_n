# Dynamic Unpivoting of a Table

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2253 |
| Difficulty | Hard |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/dynamic-unpivoting-of-a-table/) |

## Problem Description

### Goal

The wide `Products` table has primary-key column `product_id` followed by one
integer price column for each store. Store column names vary between test
cases, with between one and 30 stores. A `NULL` store cell means that product
is unavailable there.

Implement the MySQL procedure `UnpivotProducts` to return a normalized
three-column table: `product_id`, `store`, and `price`. Emit one row for every
non-null product-store price, use the source column name as `store`, and omit
unavailable combinations. Result row order is unrestricted.

### Function Contract

**Inputs**

- `Products`: A dynamically shaped table with unique integer `product_id` and one to 30 nullable integer store-price columns.

**Return value**

The `UnpivotProducts` procedure returns columns `product_id`, `store`, and
`price`, with exactly one row for each non-null store cell.

### Examples

#### Example 1

- Input columns: `product_id, LC_Store, Nozama, Shop, Souq`
- Input rows: `[(1,100,null,110,null),(2,null,200,null,190),(3,null,null,1000,1900)]`
- Output rows: `[(1,"LC_Store",100),(1,"Shop",110),(2,"Nozama",200),(2,"Souq",190),(3,"Shop",1000),(3,"Souq",1900)]`

#### Example 2

- Input columns: `product_id, Only`
- Input rows: `[(7,42)]`
- Output rows: `[(7,"Only",42)]`

#### Example 3

- Input columns: `product_id, A, B`
- Input rows: `[(1,null,null)]`
- Output rows: `[]`
