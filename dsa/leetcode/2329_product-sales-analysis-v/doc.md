# Product Sales Analysis V

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2329 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/product-sales-analysis-v/) |

## Problem Description

### Goal

The `Sales` table records which product a user purchased and in what quantity. The `Product` table gives the unit price for each referenced product. The money represented by one sale row is its quantity multiplied by that product's price.

Compute each user's total spending across all of their sale rows. Return one row per user with the columns `user_id` and `spending`. Sort users by spending from greatest to least; when two users have equal totals, place the smaller `user_id` first.

### Function Contract

**Inputs**

- `Sales`: A table with unique `sale_id` plus integer `product_id`, `user_id`, and `quantity` columns.
- `Product`: A table with unique integer `product_id` and its integer `price`.

Every `Sales.product_id` references a row in `Product`.

**Return value**

Return each `user_id` and the sum of `quantity * price` over that user's purchases. Order rows by descending `spending`, then ascending `user_id` for ties.

### Examples

**Example 1**

- Input: `Sales = [(1,1,101,10),(2,2,101,1),(3,3,102,3),(4,3,102,2),(5,2,103,3)]`, `Product = [(1,10),(2,25),(3,15)]`
- Output: `[(101,125),(102,75),(103,75)]`

User 101 has the largest total. Users 102 and 103 tie at 75, so their IDs determine their relative order.
