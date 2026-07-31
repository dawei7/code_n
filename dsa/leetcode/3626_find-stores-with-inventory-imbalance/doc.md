# Find Stores with Inventory Imbalance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3626 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/find-stores-with-inventory-imbalance/) |

## Problem Description
### Goal

The `stores` table identifies each store by `store_id` and provides its name and location. The `inventory` table lists products held by those stores, together with each product's quantity and price.

For every store having at least three different products, identify the product with the highest price and the product with the lowest price. A store has an inventory imbalance only when the highest-priced product's quantity is strictly smaller than the lowest-priced product's quantity. For each qualifying store, report its identity, both extreme products, and the ratio of the cheapest product's quantity to the most expensive product's quantity rounded to two decimal places. Order larger ratios first; equal ratios are ordered by `store_name` ascending.

### Function Contract
**Inputs**

- `stores`: Rows with unique `store_id`, plus `store_name` and `location`.
- `inventory`: Rows with unique `inventory_id`, a referenced `store_id`, `product_name`, `quantity`, and `price`.

**Return value**

Return the columns `store_id`, `store_name`, `location`, `most_exp_product`, `cheapest_product`, and `imbalance_ratio` in the required order.

### Examples
**Example 1**

- Input: Five stores whose inventories include four products for Downtown Tech, four for Suburb Mall, three for City Center, and only two each for Corner Shop and Plaza Store.
- Output: City Center with ratio `40.00`, Suburb Mall with `25.00`, and Downtown Tech with `10.00`, in that order.
- Explanation: The first three stores have at least three products and less stock of their most expensive product than of their cheapest product. The other stores fail the product-count requirement.
