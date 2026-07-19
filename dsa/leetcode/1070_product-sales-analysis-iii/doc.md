# Product Sales Analysis III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1070 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/product-sales-analysis-iii/) |

## Problem Description

### Goal

The `Sales` table stores product sales by `sale_id`, `product_id`, year, quantity, and per-unit price. Its composite primary key is `(sale_id, year)`. A product may have several sale entries in the same year.

For every product, identify the earliest year in which it appears in `Sales`, then return all of that product's sale entries from that year. Report `product_id`, the year under the name `first_year`, `quantity`, and `price`. Return the rows in any order.

### Function Contract

**Inputs**

- `Sales(sale_id, product_id, year, quantity, price)`: $R$ sale rows with composite key `(sale_id, year)`.

**Return value**

- Columns `product_id`, `first_year`, `quantity`, and `price`.
- Every sale row whose `year` equals the minimum year for its `product_id`, including multiple rows in that first year.
- Result order is unrestricted; the local reference orders by product and sale key for deterministic validation.

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

The 2009 sale for product 100 is omitted because that product already appeared in 2008.
