# Market Analysis II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1159 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/market-analysis-ii/) |

## Problem Description

### Goal

The marketplace records each user's favorite brand, every completed order, and the brand of every item. A user can buy and sell items, but this report evaluates each user in the seller role.

For every user, determine whether the second item that user sold in chronological order has the same brand as the user's favorite brand. Report `yes` when the two brands match. Report `no` when they differ or when the user sold fewer than two items. No seller sells more than one item on the same date, so each seller's second sale is unambiguous. The result may be returned in any order.

### Function Contract

**Input tables**

- `Users(user_id, join_date, favorite_brand)`: `user_id` is the primary key; users may act as both buyers and sellers.
- `Orders(order_id, order_date, item_id, buyer_id, seller_id)`: `order_id` is the primary key, `item_id` references `Items`, and both party IDs reference `Users`.
- `Items(item_id, item_brand)`: `item_id` is the primary key and identifies the sold item's brand.
- Let $r$ be the combined number of input rows across the three tables.

**Return value**

A relation containing one row per user with:

- `seller_id`: the user's ID.
- `2nd_item_fav_brand`: `yes` exactly when the user's second sale exists and its item brand equals `favorite_brand`; otherwise `no`.

### Examples

**Example 1**

`Users`

| user_id | join_date | favorite_brand |
|---:|---|---|
| 1 | 2019-01-01 | Lenovo |
| 2 | 2019-02-09 | Samsung |
| 3 | 2019-01-19 | LG |
| 4 | 2019-05-21 | HP |

`Orders`

| order_id | order_date | item_id | buyer_id | seller_id |
|---:|---|---:|---:|---:|
| 1 | 2019-08-01 | 4 | 1 | 2 |
| 2 | 2019-08-02 | 2 | 1 | 3 |
| 3 | 2019-08-03 | 3 | 2 | 3 |
| 4 | 2019-08-04 | 1 | 4 | 2 |
| 5 | 2019-08-04 | 1 | 3 | 4 |
| 6 | 2019-08-05 | 2 | 2 | 4 |

`Items`

| item_id | item_brand |
|---:|---|
| 1 | Samsung |
| 2 | Lenovo |
| 3 | LG |
| 4 | HP |

Output:

| seller_id | 2nd_item_fav_brand |
|---:|---|
| 1 | no |
| 2 | yes |
| 3 | yes |
| 4 | no |
