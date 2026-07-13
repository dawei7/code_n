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

### Required Complexity

- **Time:** $O(R \log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Identify users who follow someone**

The `follower` column names users who follow at least one account. Select its distinct values into an `active_followers` relation so each eligible user appears only once, even if that user follows several accounts.

**Count who follows each eligible user**

Join `Follow` to `active_followers` where `Follow.followee` equals the eligible user. Every joined relationship is one direct follower of that user. Group by `followee` and count the rows.

**Why this is exactly the second degree**

A grouped user necessarily appears as a followee, so at least one person follows them, and the join proves that the same user appears as a follower elsewhere. Conversely, any user with both roles appears once in `active_followers` and all rows naming that user as `followee` join to it. The count therefore includes every direct follower exactly once without multiplication from the accounts the user follows.

#### Complexity detail

For `R` relationships, distinct extraction, joining, grouping, and ordering take $O(R \log R)$ time in the general comparison-based database model and $O(R)$ execution space. Hash aggregation and suitable indexes can make the main passes near-linear.

#### Alternatives and edge cases

- **Grouped `IN` subquery:** group by `followee` and retain groups whose user occurs in `SELECT follower FROM Follow`; engines commonly materialize the subquery once, making this concise and efficient.
- **Direct self-join:** join `Follow.followee` to another row's `follower`; a user who follows several accounts multiplies direct-follower rows, so the count must use `DISTINCT` or a deduplicated role relation.
- **Correlated membership count:** rescanning all relationships for every row is correct but can take $O(R^2)$ time.
- A user who only follows others is not returned because nobody follows them.
- A user who is only followed is not returned because they follow nobody.
- Cycles are valid and can make every participant a second-degree follower.
- Following several users must not multiply the reported number of direct followers.

</details>
