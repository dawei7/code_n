# Product Sales Analysis II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1069 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/product-sales-analysis-ii/) |

## Problem Description

### Goal

The `Sales` table records product sales by `sale_id`, `product_id`, year, quantity, and per-unit price. Its composite primary key is `(sale_id, year)`, so the same product may own several distinct sale rows across years or sale identifiers.

For every product identifier that occurs in `Sales`, report the total quantity sold across all of that product's sale rows. Return `product_id` and the summed quantity under the name `total_quantity`. Result rows may be returned in any order.

### Function Contract

**Inputs**

- `Sales(sale_id, product_id, year, quantity, price)`: $R$ sale rows with composite key `(sale_id, year)`.
- `Product(product_id, product_name)`: product metadata supplied by the schema but not needed for the requested identifiers and totals.

**Return value**

- Columns `product_id` and `total_quantity`.
- One row for every distinct `product_id` occurring in `Sales`, where `total_quantity` is the sum of its `quantity` values.
- Result order is unrestricted; the local reference orders by `product_id` for deterministic validation.

### Examples

**Example 1**

`Sales`

| sale_id | product_id | year | quantity | price |
|---:|---:|---:|---:|---:|
| 1 | 100 | 2008 | 10 | 5000 |
| 2 | 100 | 2009 | 12 | 5000 |
| 7 | 200 | 2011 | 15 | 9000 |

Output:

| product_id | total_quantity |
|---:|---:|
| 100 | 22 |
| 200 | 15 |

The two rows for product 100 contribute `10 + 12`, while product 200 has one quantity of 15.
