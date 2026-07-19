# All the Pairs With the Maximum Number of Common Followers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1951 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/all-the-pairs-with-the-maximum-number-of-common-followers/) |

## Problem Description
### Goal
The `Relations` table records directed following relationships: `follower_id`
follows `user_id`. For every pair of different users, their common followers
are follower IDs that have a row for both users.

Find the greatest common-follower count attained by any user pair, then return
every pair attaining that maximum. A pair must appear once in canonical order,
with its smaller user ID first. If several pairs tie for the greatest count,
all of them belong in the result.

### Function Contract
**Inputs**

- `Relations(user_id, follower_id)`: directed follow rows whose composite
  primary key prevents duplicate relationships.

Let $R$ be the number of relation rows and $J$ the number of matched row pairs
that share a follower.

**Return value**

- A two-column table named `user1_id`, `user2_id`.
- Return every user pair with the globally maximum number of common followers.
- Emit each pair once with `user1_id < user2_id`. Row order is unrestricted.

### Examples
**Example 1**

Users 1 and 7 share followers 3, 4, and 5. The other user pairs each share only
followers 3 and 4.

- Output row: `(1, 7)`.

**Example 2**

Three users are all followed by the same two follower IDs.

- Output: all three canonical user pairs because each ties at two common
  followers.

**Example 3**

Exactly two users share one follower.

- Output: that one canonical pair.
