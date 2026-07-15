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

### Required Complexity

- **Time:** $O(r \log r)$
- **Space:** $O(r)$

<details>
<summary>Approach</summary>

#### General

**Rank sales independently for each seller.** Use `ROW_NUMBER()` partitioned by `seller_id` and ordered by `order_date`. The source guarantee that a seller has at most one sale per date makes row number `2` exactly that seller's second chronological sale. Ranking by `order_id` would be wrong because identifiers need not follow date order.

**Attach the second item's brand.** Retain the ranked order with `sale_number = 2` and join its `item_id` to `Items`. This produces at most one second-sale brand for each seller.

**Start the report from all users.** Left join the second-sale record back to `Users`, not the reverse, so users with zero or one sale remain present. Compare `item_brand` with `favorite_brand` in a `CASE` expression. Equality yields `yes`; a different brand or a null second sale falls through to `no`. Ordering by `seller_id` only stabilizes app fixtures, since the source accepts any order.

#### Complexity detail

Partitioned ranking can sort the order rows by seller and date in $O(r \log r)$ time. The subsequent primary-key joins and final projection fit within that comparison-based bound and use $O(r)$ working space for ranking and join state. Indexes or an engine-specific plan may reduce practical work without changing the query's result.

#### Alternatives and edge cases

- **Correlated second-sale lookup:** Ordering and offsetting a subquery once per user is correct, but without a suitable index it repeatedly scans `Orders` and can become quadratic.
- **Aggregate with the second minimum date:** Nested minimum calculations can work, but window ranking expresses the per-seller order directly and avoids repeated joins.
- **Use an inner join to ranked sales:** This incorrectly removes users with fewer than two sales instead of reporting `no`.
- **Rank buyer activity:** The requested role is seller; `buyer_id` does not determine a user's sold-item sequence.
- **Order IDs versus dates:** The second sale is defined by `order_date`, regardless of `order_id` values or insertion order.
- **Missing second sale:** A null item brand must produce `no`, not a null label.

</details>
