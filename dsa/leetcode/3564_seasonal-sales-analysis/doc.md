# Seasonal Sales Analysis

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3564 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/seasonal-sales-analysis/) |

## Problem Description

### Goal

Summarize product sales by meteorological season and identify the most popular product category in every season that has sales. Winter contains December, January, and February; Spring contains March through May; Summer contains June through August; and Fall contains September through November. Sales from different calendar years still belong to the same named season.

For each `(season, category)` pair, add all sold quantities and all revenue, where one sale contributes `quantity * price`. A season's winning category is the one with the greatest total quantity. If several categories have the same quantity, prefer the one with greater total revenue; if both totals tie, prefer the lexicographically smaller category.

Return one winning row per represented season. Order the rows by the season name in ascending lexicographic order.

### Function Contract

**Inputs**

- `sales`: Rows `(sale_id, product_id, sale_date, quantity, price)`, with unique `sale_id` values. `price` is the unit price for that sale.
- `products`: Rows `(product_id, product_name, category)`, with unique `product_id` values.

Every sale's `product_id` identifies its product row. Let $S$ be the number of sales rows, $P$ the number of product rows, and $G$ the number of distinct `(season, category)` groups represented by the joined sales.

**Return value**

Return columns `season`, `category`, `total_quantity`, and `total_revenue`. Include the highest-ranked category for each represented season and order the result by `season` ascending.

### Examples

#### Example 1

- **Input:** Sales span all four seasons and products belong to Apparel, Kitchen, Tech, and Fitness.
- **Output:** `[(Fall,Apparel,10,120.00), (Spring,Kitchen,3,54.00), (Summer,Tech,5,100.00), (Winter,Apparel,9,110.00)]`
- **Explanation:** Quantity selects the winner except in Summer, where Tech and Fitness each sell five units; Tech wins because its revenue is higher.

---
