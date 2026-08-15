# Friday Purchases I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2993 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/friday-purchases-i/) |

## Problem Description

### Goal

The `Purchases` table records a user, a purchase date, and an amount. Every
date lies between November 1 and November 30, 2023, inclusive, and the triple
`(user_id, purchase_date, amount_spend)` is unique.

For each Friday in that month having at least one purchase, sum all spending
on that date. Return its one-based `week_of_month`, the `purchase_date`, and
the `total_amount`. Weeks without a Friday purchase must not appear. Order the
result by week of month ascending.

### Function Contract

**Inputs**

- `Purchases(user_id, purchase_date, amount_spend)`: November 2023 purchase rows

Let $R$ be the number of purchase rows.

**Return value**

Return one ordered row for every Friday date represented in the table.

### Examples

#### Example 1

- **Input:** Purchases include `5117` on November 3 and `9692` plus `12000` on November 24.
- **Output:** `(1,"2023-11-03",5117)` and `(4,"2023-11-24",21692)`

#### Example 2

- **Input:** Purchases only on non-Friday dates.
- **Output:** No rows.

#### Example 3

- **Input:** Purchases on November 3, 10, 17, and 24.
- **Output:** Weeks `1`, `2`, `3`, and `4` respectively.
