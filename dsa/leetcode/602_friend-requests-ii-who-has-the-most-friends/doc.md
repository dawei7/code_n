# Friend Requests II: Who Has the Most Friends

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 602 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/) |

## Problem Description
### Goal
Given a `RequestAccepted` table of accepted friend requests, find the person who has the most friends. Each accepted row forms one undirected friendship between `requester_id` and `accepter_id`, so the relationship contributes one friend to both people regardless of who originally sent the request.

Return two columns: `id` for the most-connected person and `num` for that person's number of friends. The test data guarantees that only one person has the most friends, so the result contains a single winner and requires no tie-breaking rule.

### Function Contract
**Inputs**

- `RequestAccepted(requester_id, accepter_id, accept_date)`: accepted friend requests connecting two users

**Return value**

- Columns `id` and `num`, where `id` is the uniquely most-connected user and `num` is that user's friend count
- An accepted request contributes one friend to both endpoint users

### Examples
**Example 1**

- Input: accepted pairs `(1,2), (1,3), (2,3), (3,4)`
- Output: `id = 3, num = 3`

**Example 2**

- Input: users 2, 3, and 4 each send an accepted request to user 5
- Output: `id = 5, num = 3`

**Example 3**

- Input: one user appears as both requester and accepter across several pairs
- Output: count all incident accepted pairs for that user

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Treat friendship as an undirected connection**

Although each row stores a requester and an accepter, both users gain one friend when the request is accepted. Each endpoint must therefore contribute one occurrence to its user's total.

**Normalize both endpoint columns**

Select every `requester_id` as a common `id` column, then combine it with every `accepter_id` using `UNION ALL`. Keeping all occurrences is essential because each row represents one friendship contribution.

**Count normalized occurrences**

Group the combined endpoint stream by `id`. The group size is exactly that user's number of incident accepted requests. Order counts descending and retain the first row; the contract guarantees a unique maximum.

**Why the winning count is exact**

Every accepted friendship produces precisely two normalized rows, one for each endpoint. Thus a user's normalized occurrences are in one-to-one correspondence with that user's friends in the accepted-pair table. Grouping calculates all exact degrees, and the descending first group is the unique maximum.

#### Complexity detail

For `n` accepted requests, normalization creates `2n` endpoint rows. Grouping and ordering generally take $O(n \log n)$ time and $O(n)$ working space.

#### Alternatives and edge cases

- **Aggregate each endpoint column first:** count requesters and accepters separately, union those partial totals, then sum by user; it has the same asymptotic bound.
- **Correlated incident-edge count per user:** is correct but may rescan all requests for every distinct user and take $O(n^2)$ time.
- **Use `UNION` instead of `UNION ALL`:** incorrectly removes repeated endpoint occurrences and undercounts users with several friends.
- **User in both columns:** contributions from both roles must be added.
- **Nonconsecutive user identifiers:** are ordinary grouping keys.
- **One accepted pair per friendship:** each endpoint gains one count.
- **Unique winner guarantee:** no tie-breaker should determine the result.

</details>
