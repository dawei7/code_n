# Users With Two Purchases Within Seven Days

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2228 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/users-with-two-purchases-within-seven-days/) |

## Problem Description

### Goal

The `Purchases` table records retailer transactions. Each row has a unique `purchase_id`, the `user_id` that made the purchase, and its `purchase_date`.

Report every user who has at least one pair of distinct purchases whose dates are at most seven days apart. Purchases on the same date qualify, as does a pair exactly seven days apart. Return each qualifying `user_id` once, with the result ordered by `user_id`.

### Function Contract

**Inputs**

- `Purchases`: Rows with integer `purchase_id`, integer `user_id`, and date-valued `purchase_date`.

Let $r$ be the number of purchase rows.

**Return value**

Return one `user_id` column containing each qualifying user exactly once, ordered in ascending numeric order.

### Examples

#### Example 1

- **Input:** purchases `(4, 2, "2022-03-13")`, `(1, 5, "2022-02-11")`, `(3, 7, "2022-06-19")`, `(6, 2, "2022-03-20")`, `(5, 7, "2022-06-19")`, `(2, 2, "2022-06-08")`
- **Output:** users `2` and `7`

#### Example 2

- **Input:** one user purchases on `"2024-01-01"` and `"2024-01-08"`
- **Output:** that user, because the dates are exactly seven days apart

#### Example 3

- **Input:** one user purchases on `"2024-01-01"` and `"2024-01-09"`
- **Output:** no rows, because the only pair is eight days apart
