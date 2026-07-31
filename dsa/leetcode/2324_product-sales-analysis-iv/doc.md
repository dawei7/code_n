# Product Sales Analysis IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2324 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/product-sales-analysis-iv/) |

## Problem Description

### Goal

The `Sales` table records product purchases, including the buyer and quantity. The `Product` table supplies the unit price of every referenced product. A user may have multiple sale rows for the same product, so that user's total spending on the product is the sum of `quantity * price` across all such rows.

For every user, report the product or products on which that user spent the greatest total amount. If multiple products tie for a user's maximum, include every tied product. Return only the user and product identifiers; the result rows may appear in any order.

### Function Contract

**Inputs**

- `Sales`: A table with unique `sale_id` plus integer `product_id`, `user_id`, and `quantity` columns.
- `Product`: A table with unique integer `product_id` and its integer `price`.

Every product referenced by `Sales` exists in `Product`.

**Return value**

Return columns `user_id` and `product_id` for every product whose cumulative spending equals that user's maximum cumulative spending. Result order is unrestricted.

### Examples

**Example 1**

- Input: `Sales = [(1,1,101,10),(2,3,101,7),(3,1,102,9),(4,2,102,6),(5,3,102,10),(6,1,102,6)]`, `Product = [(1,10),(2,25),(3,15)]`
- Output: `[(101,3),(102,1),(102,2),(102,3)]`

User 101 spends 105 on product 3 versus 100 on product 1. User 102 spends 150 on each of the three products, so all three are returned.
