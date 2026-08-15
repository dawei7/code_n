# The Number of Users That Are Eligible for Discount

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2205 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/the-number-of-users-that-are-eligible-for-discount/) |

## Problem Description

### Goal

The `Purchases` table records the user, timestamp, and amount of every purchase. A user is eligible for a discount when at least one of their purchases both falls within a requested inclusive time interval and reaches a requested minimum amount.

Count the distinct eligible users. The supplied `startDate` and `endDate` values are dates interpreted at the start of their respective days. Consequently, a purchase exactly at midnight on `endDate` is included, while a purchase later during that calendar date is after the interval.

### Function Contract

**Inputs**

- `Purchases(user_id, time_stamp, amount)`: purchase records whose composite primary key is `(user_id, time_stamp)`.
- `startDate`: the inclusive lower timestamp boundary, interpreted as midnight.
- `endDate`: the inclusive upper timestamp boundary, interpreted as midnight.
- `minAmount`: the inclusive minimum qualifying purchase amount.

For cOde(n)'s SQLite fixtures, the three scalar arguments are supplied as the single row of `Parameters(startDate, endDate, minAmount)`. The native LeetCode artifact preserves the required MySQL `getUserIDs` stored-function declaration.

**Return value**

Return one row with column `user_cnt`, containing the number of distinct users who have at least one qualifying purchase.

### Examples

#### Example 1

- **Input:** `startDate = "2022-03-08"`, `endDate = "2022-03-20"`, `minAmount = 1000`, with purchases by users 1, 2, and 3
- **Output:** `1`
- **Explanation:** only user 3 has an amount of at least `1000` within the interval.

#### Example 2

- **Input:** one user buys at `2024-06-30 00:00:00` and again at `2024-06-30 10:00:00`, with `endDate = "2024-06-30"`
- **Output:** `1`
- **Explanation:** the midnight purchase is inside the interval; the later purchase on the named end date is not.

#### Example 3

- **Input:** several qualifying purchases belong to the same user
- **Output:** that user contributes `1`
- **Explanation:** eligibility is counted per distinct user, not per purchase.
