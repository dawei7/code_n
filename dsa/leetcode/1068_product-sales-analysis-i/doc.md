# Product Sales Analysis I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1068 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/product-sales-analysis-i/) |

## Problem Description

### Goal

The `Sales` table records each sale using a composite primary key `(sale_id, year)`. Every row identifies a product, the sale year, quantity, and per-unit price. Its `product_id` refers to the corresponding row in `Product`, where each product identifier has one product name.

For every row in `Sales`, report the associated `product_name` together with that sale's `year` and `price`. Preserve separate sale rows even when they reference the same product or share the same price. Return the resulting table in any order.

### Function Contract

**Inputs**

- `Sales(sale_id, product_id, year, quantity, price)`: $R$ sale rows; `(sale_id, year)` is the composite primary key and `price` is per unit.
- `Product(product_id, product_name)`: $P$ product rows keyed by `product_id`.
- Every `Sales.product_id` references a row in `Product`.

**Return value**

- Columns `product_name`, `year`, and `price`, with one output row for every sale.
- Result order is unrestricted; the local reference orders by the sale key for deterministic validation.

### Examples

**Example 1**

`Sales`

| sale_id | product_id | year | quantity | price |
|---:|---:|---:|---:|---:|
| 1 | 100 | 2008 | 10 | 5000 |
| 2 | 100 | 2009 | 12 | 5000 |
| 7 | 200 | 2011 | 15 | 9000 |

`Product`

| product_id | product_name |
|---:|---|
| 100 | Nokia |
| 200 | Apple |
| 300 | Samsung |

Output:

| product_name | year | price |
|---|---:|---:|
| Nokia | 2008 | 5000 |
| Nokia | 2009 | 5000 |
| Apple | 2011 | 9000 |

The Samsung product has no sale row, while both Nokia sale rows remain separate.
