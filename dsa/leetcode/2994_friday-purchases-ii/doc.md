# Friday Purchases II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2994 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/friday-purchases-ii/) |

## Problem Description

### Goal

The `Purchases` table records a user, a purchase date, and an amount. Every
date is between November 1 and November 30, 2023, inclusive, and the triple
`(user_id, purchase_date, amount_spend)` is unique.

Report total user spending on each Friday of November 2023. All four Fridays
must appear: when no purchase occurred on a Friday, its total is `0`. Return
the one-based `week_of_month`, the Friday `purchase_date`, and `total_amount`,
ordered by week ascending.

### Function Contract

**Inputs**

- `Purchases(user_id, purchase_date, amount_spend)`: November 2023 purchase rows

Let $R$ be the number of purchase rows.

**Return value**

Return exactly four ordered rows for November 3, 10, 17, and 24, using zero
for a Friday without purchases.

### Examples

#### Example 1

- **Input:** Spending of `5117` on November 3 and `9692 + 12000` on November 24
- **Output:** Weeks `1` and `4` have totals `5117` and `21692`; weeks `2` and `3` have `0`.

#### Example 2

- **Input:** Purchases only on non-Friday dates
- **Output:** Four Friday rows, all with total `0`.

#### Example 3

- **Input:** Purchases on all four Fridays
- **Output:** Their four independently summed totals.
