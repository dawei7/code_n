# Market Analysis I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1158 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/market-analysis-i/) |

## Problem Description

### Goal

The marketplace stores its members in `Users`, every purchase in `Orders`, and item brands in `Items`. Users may participate in orders as buyers or sellers, but this report concerns only purchases they made as buyers.

For every user, return the user's ID, join date, and number of orders placed as a buyer during calendar year 2019. Users with no qualifying order must still appear with a count of zero. The `Items` data and favorite brands do not affect this report. The result may be returned in any order.

### Function Contract

**Input tables**

- `Users(user_id, join_date, favorite_brand)`: `user_id` is the primary key; each row describes one marketplace user.
- `Orders(order_id, order_date, item_id, buyer_id, seller_id)`: `order_id` is the primary key, `item_id` references `Items`, and both user IDs reference `Users`.
- `Items(item_id, item_brand)`: `item_id` is the primary key.
- Let $r$ be the combined number of rows in `Users` and `Orders`, the only tables the report needs to inspect.

**Return value**

A relation with these columns:

- `buyer_id`: the user's ID.
- `join_date`: that user's stored join date.
- `orders_in_2019`: the number of the user's buyer-side orders dated from January 1 through December 31, 2019.

### Examples

**Example 1**

`Users`

| user_id | join_date | favorite_brand |
|---:|---|---|
| 1 | 2018-01-01 | Lenovo |
| 2 | 2018-02-09 | Samsung |
| 3 | 2018-01-19 | LG |
| 4 | 2018-05-21 | HP |

`Orders`

| order_id | order_date | item_id | buyer_id | seller_id |
|---:|---|---:|---:|---:|
| 1 | 2019-08-01 | 4 | 1 | 2 |
| 2 | 2018-08-02 | 2 | 1 | 3 |
| 3 | 2019-08-03 | 3 | 2 | 3 |
| 4 | 2018-08-04 | 1 | 4 | 2 |
| 5 | 2018-08-04 | 1 | 3 | 4 |
| 6 | 2019-08-05 | 2 | 2 | 4 |

Output:

| buyer_id | join_date | orders_in_2019 |
|---:|---|---:|
| 1 | 2018-01-01 | 1 |
| 2 | 2018-02-09 | 2 |
| 3 | 2018-01-19 | 0 |
| 4 | 2018-05-21 | 0 |
