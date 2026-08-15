# Friends With No Mutual Friends

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3058 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/friends-with-no-mutual-friends/) |

## Problem Description

### Goal

The `Friends` table stores pairs of users who are friends with each other. A
third user is a mutual friend of a pair when that third user is directly
connected to both endpoints.

Find every stored friendship whose two users have no mutual friend. Friendship
is undirected even though its endpoints occupy two separate columns, so a
connection must be recognized from either orientation. Return the original
`user_id1` and `user_id2` values, ordered by both columns ascending.

### Function Contract

**Inputs**

- `Friends(user_id1, user_id2)`: each unique pair records one undirected
  friendship between two users.

Let $m$ be the number of friendship rows and $d$ the maximum number of friends
belonging to any one user.

**Return value**

- An ordered table with columns `user_id1` and `user_id2`, containing precisely
  the stored pairs whose endpoints have no common neighbor.

### Examples

#### Example 1

In the supplied network, pairs such as `(1, 2)` are excluded because user `5`
is connected to both endpoints. Pairs `(6, 7)` and `(8, 9)` have no mutual
friend, so they are returned in identifier order.

#### Example 2

A single friendship has no third user connected to both endpoints and is
therefore returned.

#### Example 3

Every edge of a triangle is excluded: for each pair, the triangle's remaining
vertex is a mutual friend.
