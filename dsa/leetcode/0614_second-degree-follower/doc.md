# Second Degree Follower

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 614 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/second-degree-follower/) |

## Problem Description
### Goal
Given a `Follow` table where each row means that `follower` follows `followee`, find the users who appear as followers themselves and also have one or more people directly following them. These users form the second degree of a follow chain: they follow another user while serving as a followee for others.

For every such user, return their identifier in a column named `follower` and the number of their direct followers in `num`. Count unique stored relationships and order the result by `follower`. Users who follow someone but have no followers of their own are omitted.

### Function Contract
**Inputs**

- `Follow(followee, follower)`: each row states that `follower` follows `followee`; each ordered relationship is unique

**Return value**

- `follower`: a user who appears in both relationship roles
- `num`: that user's number of direct followers
- Rows are ordered by `follower`

### Examples
**Example 1**

- Input relationships: Bob follows Alice; Cena and Donald follow Bob; Edward follows Donald
- Output rows: `(Bob, 2)`, `(Donald, 1)`

**Example 2**

- Input relationships: A follows B and B follows A
- Output rows: `(A, 1)`, `(B, 1)`
