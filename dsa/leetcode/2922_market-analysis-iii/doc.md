# Market Analysis III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2922 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/market-analysis-iii/) |

## Problem Description

### Goal

The marketplace records sellers in `Users`, product brands in `Items`, and
individual sales in `Orders`. For each seller, consider only orders whose
item brand differs from that seller's favorite brand. Count the number of
distinct item IDs among those qualifying orders, so repeated sales of the same
item contribute once.

Find the largest such count and return every seller attaining it. The result
must contain `seller_id` and the count as `num_items`, ordered by
`seller_id` in ascending order. Sellers without a qualifying sale do not
produce a grouped count.

### Function Contract

**Inputs**

- `Users(seller_id, join_date, favorite_brand)`: One row per seller;
  `seller_id` is unique.
- `Items(item_id, item_brand)`: One row per item; `item_id` is unique.
- `Orders(order_id, order_date, item_id, seller_id)`: One row per order;
  `order_id` is unique, and the item and seller columns reference the other
  two tables.

Let $U$, $I$, and $O$ be the row counts of `Users`, `Items`, and `Orders`,
and let $W$ be the number of winning sellers.

**Return value**

- An ordered table with columns `seller_id` and `num_items`, containing all
  sellers tied for the greatest positive distinct mismatched-brand item count.

### Examples

#### Example 1

For the supplied market, seller 2 sells mismatched item 4 twice and favorite-
brand item 1 once; the distinct qualifying count is therefore one. Seller 3
sells mismatched item 2 and favorite-brand item 3, also giving one. The ordered
result is:

| seller_id | num_items |
|---:|---:|
| 2 | 1 |
| 3 | 1 |

#### Example 2

If seller 1, whose favorite brand is `A`, repeatedly sells item 1 of brand
`C` and also sells item 2 of brand `B`, those orders represent two distinct
qualifying items regardless of repetition.

#### Example 3

If every seller sells only items matching their own favorite brand, no order
passes the brand filter and the result is empty.
