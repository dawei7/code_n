# Popularity Percentage

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2720 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/popularity-percentage/) |

## Problem Description

### Goal

The `Friends` table stores friendships between pairs of users on a social platform. A friendship is undirected: if a row contains `user1 = a` and `user2 = b`, then each user counts the other as a friend even though the reverse row need not be present.

For every user appearing anywhere in the table, compute the user's number of distinct friends divided by the total number of distinct platform users, multiply that ratio by $100$, and round the result to two decimal places. Return one row per user under the column name `percentage_popularity`, ordered by `user1` in ascending order.

### Function Contract

Let $R$ be the number of rows in `Friends`.

**Inputs**

- `Friends`: A table with integer columns `user1` and `user2`. Their pair is the primary key, and each row records a friendship between the two users.

**Return value**

Return the columns `user1` and `percentage_popularity`. The percentage equals the user's distinct friend count divided by the number of distinct users appearing in either input column, multiplied by $100$ and rounded to two decimal places. Sort by `user1` in ascending order.

### Examples

#### Example 1

- **Input:** The nine sample friendship rows connect users $1$ through $9$.
- **Output:** User $1$ has popularity $55.56$, users $2$ and $3$ each have $33.33$, and the remaining rows follow their friend counts.
- **Explanation:** User $1$ has five distinct friends among nine total users, so $(5/9)\cdot100$ rounds to $55.56$.

#### Example 2

- **Input:** `Friends = [(10, 20)]`
- **Output:** `(10, 50.00)` and `(20, 50.00)`
- **Explanation:** Each of the two users has one friend among two platform users.

#### Example 3

- **Input:** `Friends = [(1, 2), (2, 3)]`
- **Output:** `(1, 33.33)`, `(2, 66.67)`, and `(3, 33.33)`
- **Explanation:** The middle user has two friends, while each endpoint has one.
