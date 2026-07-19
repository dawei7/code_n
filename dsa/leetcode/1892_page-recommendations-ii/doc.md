# Page Recommendations II

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/page-recommendations-ii/) |
| Frontend ID | 1892 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

`Friendship` stores pairs of users who are friends, and each friendship applies in both directions even though it is recorded as one row. `Likes` records which pages each user likes. Both tables use their two columns as composite primary keys, so a friendship pair or user-page like is not duplicated.

For every user participating in the friendship graph, recommend each page liked by at least one of that user's friends but not already liked by the user. Return one row per recommended user-page pair and count how many of the user's friends like that page as `friends_likes`. Result rows may appear in any order.

### Function Contract

**Inputs**

- `Friendship(user1_id, user2_id)`: one row per undirected friendship.
- `Likes(user_id, page_id)`: one row per distinct user-page like.
- Let $F$ be the number of friendship rows, $L$ the number of like rows, and $C$ the number of friend-like candidate rows produced after expanding friendships in both directions.

**Return value**

- Return columns `user_id`, `page_id`, and `friends_likes`.
- Include a user-page pair exactly when at least one friend likes the page and the user does not.
- Set `friends_likes` to the number of that user's friends who like the page.
- Output order is not significant.

### Examples

**Example 1**

- Input: users `1` and `2` share friends `3` and `4`; users `2` and `3` both like page `77`; user `1` already likes page `88`.
- Output includes `(1,77,2)` because two friends of user `1` like page `77`, but it excludes `(1,88,...)` because user `1` already likes page `88`.

**Example 2**

- Input: friendship `(1,2)`, with only user `2` liking page `10`.
- Output: `(1,10,1)`.

The stored orientation does not prevent recommending user `1` a page liked by user `2`.

**Example 3**

- Input: friendship `(1,2)`, and both users like page `10`.
- Output: no rows.

The friend's like cannot recommend a page the target user already likes.
