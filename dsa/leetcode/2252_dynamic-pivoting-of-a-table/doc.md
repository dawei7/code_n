# Dynamic Pivoting of a Table

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2252 |
| Difficulty | Hard |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/dynamic-pivoting-of-a-table/) |

## Problem Description

### Goal

The `Products` table contains one row for each available `(product_id, store)`
pair, together with that product's `price` at the store. The pair is the
primary key, and the table contains at most 30 distinct store names.

Implement the MySQL procedure `PivotProducts` so each output row represents
one product. After `product_id`, create one column for every store found in the
current table, with store columns sorted in lexicographical order. A cell
contains the product's price at that store or `null` when the store does not
sell the product. Output row order is unrestricted.

### Function Contract

**Inputs**

- `Products`: A table with integer `product_id`, string `store`, and integer `price`; `(product_id, store)` is unique and at most 30 stores occur.

**Return value**

The `PivotProducts` procedure returns one row per product with `product_id`
first, followed by dynamically generated store columns in lexicographical
order and nullable prices.

### Examples

#### Example 1

- **Input:** `Products = [(1,"Shop",110),(1,"LC_Store",100),(2,"Nozama",200),(2,"Souq",190),(3,"Shop",1000),(3,"Souq",1900)]`
- Output columns: `product_id, LC_Store, Nozama, Shop, Souq`
- Output rows: `[(1,100,null,110,null),(2,null,200,null,190),(3,null,null,1000,1900)]`

#### Example 2

- **Input:** `Products = [(7,"Only",42)]`
- Output columns: `product_id, Only`
- Output rows: `[(7,42)]`

#### Example 3

- **Input:** `Products = [(1,"B",20),(2,"A",30)]`
- Output columns: `product_id, A, B`
- Output rows: `[(1,null,20),(2,30,null)]`
