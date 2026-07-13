# Market Analysis II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1159 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [market-analysis-ii](https://leetcode.com/problems/market-analysis-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/market-analysis-ii/).

### Goal
For every user treated as a possible seller, determine whether the item in their second sale has the same brand as their favorite brand. Users with fewer than two sales should be reported as `no`.

### Query Contract
**Input tables**

- `Users(user_id, join_date, favorite_brand)`: Marketplace users.
- `Orders(order_id, order_date, item_id, buyer_id, seller_id)`: Orders between users.
- `Items(item_id, item_brand)`: Item brand metadata.

**Output columns**

- `seller_id`
- `2nd_item_fav_brand`

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

---

## Solution
### Approach
Rank each seller's orders by `order_date` using a window function. Keep the row with rank `2`, join it to `Items`, and compare the sold item's brand with the seller's `favorite_brand`.

Left join that second-sale information back to all users so sellers with fewer than two sales produce `no`.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, orders are partitioned by seller and ranked.
- **Space Complexity**: Depends on the execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
