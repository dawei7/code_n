# Friday Purchase III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3118 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/friday-purchase-iii/) |

## Problem Description

### Goal

The `Purchases` table records a user, a November 2023 purchase date, and the amount spent. Its composite primary key is (`user_id`, `purchase_date`, `amount_spend`). The `Users` table maps each unique `user_id` to one of the membership categories `Standard`, `Premium`, or `VIP`.

For each of the four Fridays in November 2023, calculate the total amount spent separately by `Premium` and `VIP` members. Every Friday-membership pair must appear even when its total is zero. Return `week_of_month`, `membership`, and `total_amount`, ordered by `week_of_month` and then by `membership`, both in ascending order.

### Function Contract

**Inputs**

- `Purchases`: Rows with integer `user_id`, date `purchase_date`, and integer `amount_spend`; dates range from November 1 through November 30, 2023.
- `Users`: One row per `user_id`, with `membership` in `Standard`, `Premium`, or `VIP`.

Let $p$ be the number of rows in `Purchases` and $u$ the number of rows in `Users`.

**Return value**

Return exactly eight rows with columns `week_of_month`, `membership`, and `total_amount`: two membership rows for each Friday, including zero totals. Sort first by `week_of_month` ascending and then by `membership` ascending.

### Examples

#### Example 1

- **Input:** Purchases on November 3, 10, 17, and 24 by users from all three membership categories.
- **Output:** Eight rows covering weeks 1 through 4 and memberships `Premium` and `VIP`.
- **Explanation:** A `Premium` purchase of `1126` on November 3 produces `(1, Premium, 1126)`, while the missing `VIP` total for that Friday is reported as zero.

#### Example 2

- **Input:** No `Premium` or `VIP` member purchases anything on November 17.
- **Output:** `(3, Premium, 0)` and `(3, VIP, 0)` are both present.
- **Explanation:** Missing fact rows do not remove required Friday-membership combinations.

#### Example 3

- **Input:** `VIP` members spend `9692` and `5241` on November 24.
- **Output:** `(4, VIP, 14933)`.
- **Explanation:** All qualifying purchases for the same Friday and membership are summed.
