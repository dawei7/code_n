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
