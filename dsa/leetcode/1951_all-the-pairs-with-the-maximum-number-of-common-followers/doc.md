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

### Required Complexity
- **Time:** $O(R+J\log J)$
- **Space:** $O(J)$

<details>
<summary>Approach</summary>

#### General

**Generate canonical pairs through shared followers**

Self-join `Relations` on equal `follower_id`. Require the first row's
`user_id` to be smaller than the second row's `user_id`. Every joined row then
represents one follower shared by one canonical user pair, with no mirrored
copy and no pairing of a user with itself.

Group by those two user IDs and count the joined rows. The composite primary
key guarantees that one follower contributes at most once to one pair, so the
group count is exactly the number of common followers.

**Keep every maximum tie**

Rank the grouped pairs by common-follower count in descending order using
`DENSE_RANK`. All pairs with the greatest count receive rank 1, including ties.
Filter to that rank and project only the two required user-ID columns.

#### Complexity detail

Reading the source takes $O(R)$ work. The self-join produces $J$ matched
follower-pair rows, and a sort-based grouping and ranking plan costs
$O(J\log J)$ time and $O(J)$ working space. Appropriate indexes or hash
aggregation can reduce practical join and grouping costs.

#### Alternatives and edge cases

- **Cross-join every user pair:** Generate all users twice and calculate an
  intersection for every pair. It is correct but performs quadratic work even
  for pairs with no shared follower.
- **Use `LIMIT 1`:** Returning only one highest-count group loses other pairs
  tied for the maximum.
- **Use `ROW_NUMBER`:** It assigns distinct ranks to tied rows; `DENSE_RANK`
  or comparison with `MAX` is required to preserve all ties.
- The strict user-ID inequality both removes self-pairs and fixes output
  orientation.
- A follower shared by several users generates one contribution for each
  distinct pair among those users.
- A user ID may also appear as a follower ID; the columns' roles remain
  independent.
- Input row order has no effect on grouping or ranking.

</details>
