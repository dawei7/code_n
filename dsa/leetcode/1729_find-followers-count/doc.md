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

### Required Complexity

- **Time:** $O(R)$
- **Space:** $O(U)$

<details>
<summary>Approach</summary>

#### General

**Group relationships by the followed user**

Group the table by `user_id`. Every row in one group represents one distinct follower relationship because the composite primary key forbids duplicates. `COUNT(follower_id)` therefore gives exactly that user's number of followers.

No separate users table participates in the query, so the result contains precisely the `user_id` values represented by at least one relationship. A user absent from `Followers` cannot be inferred and does not produce a zero-count row.

**Name and order the result explicitly**

Alias the aggregate as `followers_count`, then order the grouped rows by `user_id ASC`. The declared primary key begins with `user_id`, allowing an engine to scan relationships in grouping and output order, but the explicit `ORDER BY` remains necessary to make the result contract deterministic.

#### Complexity detail

Every one of the $R$ relationships must be inspected because any row can change one user's count. Hash aggregation performs expected constant work per row and stores at most $U$ counters, taking $O(R)$ time and $O(U)$ space. An ordered scan of the composite primary-key index can instead aggregate consecutive users while already producing ascending order.

#### Alternatives and edge cases

- **Correlated count per user:** Selecting distinct users and rescanning `Followers` for each one can take $O(RU)$ time without a suitable index.
- **Window count plus deduplication:** A window function can attach the group count to every relationship, but an additional distinct step is needed to return one row per user.
- **Single relationship:** Its user receives a follower count of one.
- **Shared follower:** One `follower_id` may follow several users and contributes once to each corresponding group.
- **Nonconsecutive identifiers:** Grouping and numeric ordering do not assume contiguous user IDs.
- **Duplicate relationship:** The primary key rules it out, so ordinary `COUNT` is sufficient; `COUNT(DISTINCT follower_id)` is unnecessary.
- **Missing users:** With no separate user table, users having zero recorded followers do not appear.

</details>
