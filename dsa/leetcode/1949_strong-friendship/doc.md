# Strong Friendship

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1949 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/strong-friendship/) |

## Problem Description
### Goal
The `Friendship` table stores undirected friendships. Each pair is recorded
once in canonical order, with the smaller user ID in `user1_id` and the larger
one in `user2_id`.

An existing friendship is strong when its two users have at least three common
friends. Find every strong friendship and report the number of common friends
for that pair. A pair that is not itself present in `Friendship` must not be
returned, even if those users share several friends.

### Function Contract
**Inputs**

- `Friendship(user1_id, user2_id)`: one row per undirected friendship.
  `(user1_id, user2_id)` is the primary key and every row satisfies
  `user1_id < user2_id`.

Let $E$ be the number of friendship rows, and let $W$ be the number of
neighbor-pair matches examined while intersecting adjacency lists.

**Return value**

- A table with columns `user1_id`, `user2_id`, and `common_friend`.
- Include exactly the existing friendship pairs with at least three common
  friends; `common_friend` is that common-neighbor count.
- Each pair appears once with `user1_id < user2_id`. Row order is unrestricted.

### Examples
**Example 1**

For the published friendship graph, users 1 and 2 share users 3, 4, 5, and 6,
while users 1 and 3 share users 2, 6, and 7.

- Output rows: `(1, 2, 4)` and `(1, 3, 3)`.

**Example 2**

An existing pair shares exactly users 3, 4, and 5.

- Output row: that pair with `common_friend = 3`.

**Example 3**

Every friendship has fewer than three common friends.

- Output: no rows.
