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

### Required Complexity
- **Time:** $O(E+W\log W)$
- **Space:** $O(E+W)$

<details>
<summary>Approach</summary>

#### General

**Expand each undirected friendship**

Create a `connections` common table expression with both orientations of every
stored edge. A row `(user_id, friend_id)` then means that `friend_id` belongs
to `user_id`'s adjacency list, regardless of which endpoint was smaller in the
source row.

**Intersect adjacency lists for stored pairs**

Begin with each row of `Friendship`. Join its first endpoint to one copy of
`connections` and its second endpoint to another copy. Require the two
connection rows to have the same `friend_id`. Every resulting joined row
identifies one user adjacent to both endpoints, and only source friendship
rows can produce groups.

Group by the canonical stored pair and count the matches. The primary-key
guarantee and doubled orientation give exactly one connection row per directed
adjacency, so `COUNT(*)` counts distinct common friends without an additional
deduplication step. Retain groups whose count is at least three.

#### Complexity detail

Expanding the table creates $2E$ directed rows. The adjacency intersections
examine $W$ matching neighbor combinations; grouping them takes
$O(W\log W)$ in a sort-based execution, for $O(E+W\log W)$ total time.
Materializing directed edges and grouped matches uses $O(E+W)$ working space.
Database indexes and hash aggregation may reduce the practical lookup or
grouping cost.

#### Alternatives and edge cases

- **Generate all user pairs:** Cross-join every distinct user, count shared
  neighbors, then test whether the pair is a friendship. It is correct but
  wastes quadratic work on pairs that are not stored edges.
- **Store only the original orientation:** Joining directly on `user1_id` or
  `user2_id` misses friendships where a user appears in the opposite column.
- Exactly three common friends qualifies because the threshold is inclusive.
- A common neighbor may have an ID smaller than, between, or larger than the
  two endpoints; orientation expansion handles all cases.
- A non-friend pair is excluded regardless of its number of common neighbors.
- The result count is not the endpoints' total degree; only neighbors shared
  by both users contribute.
- An empty table or a graph without qualifying triangles produces no rows.

</details>
