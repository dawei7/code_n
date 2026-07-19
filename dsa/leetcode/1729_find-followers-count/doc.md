# Find Followers Count

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1729 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-followers-count/) |

## Problem Description

### Goal

The `Followers` table records directed relationships in a social-media application. Each row `(user_id, follower_id)` means that `follower_id` follows `user_id`. The pair of identifiers is the table's primary key, so the same follower relationship cannot appear more than once.

For every `user_id` appearing in the table, count its follower rows. Return one row per user with the columns `user_id` and `followers_count`, ordered by `user_id` in ascending order.

### Function Contract

**Inputs**

- `Followers(user_id, follower_id)`: one row per unique directed following relationship, with `(user_id, follower_id)` as the composite primary key.

Let $R$ be the number of relationship rows and $U$ the number of distinct `user_id` values.

**Return value**

- Return a table with columns `user_id` and `followers_count`, containing one row for each represented user and ordered by `user_id` in ascending order.

### Examples

**Example 1**

- Input: relationships `(0,1)`, `(1,0)`, `(2,0)`, and `(2,1)`
- Output: `(0,1)`, `(1,1)`, and `(2,2)`
- Explanation: Users `0` and `1` each have one follower, while user `2` has two.

**Example 2**

- Input: the single relationship `(7,42)`
- Output: `(7,1)`
- Explanation: The only represented user has one follower.

**Example 3**

- Input: relationships for users `10` and `3`, supplied in mixed row order
- Output: the row for user `3` before the row for user `10`
- Explanation: Output order follows `user_id`, not input order or follower identifiers.
