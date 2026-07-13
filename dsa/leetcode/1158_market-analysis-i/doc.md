# Market Analysis I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1158 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [market-analysis-i](https://leetcode.com/problems/market-analysis-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/market-analysis-i/).

### Goal
For every user, report their join date and how many orders they placed as a buyer during calendar year 2019.

### Query Contract
**Input tables**

- `Users(user_id, join_date, favorite_brand)`: Marketplace users.
- `Orders(order_id, order_date, item_id, buyer_id, seller_id)`: Orders between users.
- `Items(item_id, item_brand)`: Item brand metadata.

**Output columns**

- `buyer_id`
- `join_date`
- `orders_in_2019`

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

---

## Solution
### Approach
Start from `Users` so users with zero matching orders remain present. Left join to `Orders` restricted to dates from `2019-01-01` through `2019-12-31`, group by user, and count matching order ids.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, orders are filtered and aggregated by buyer.
- **Space Complexity**: Depends on the execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
