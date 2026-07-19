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

### Required Complexity

- **Time:** $O((F+L+C)\log C)$
- **Space:** $O(F+L+C)$

<details>
<summary>Approach</summary>

#### General

**Normalize the undirected graph**

Create a common table expression containing `(user_id, friend_id)` in both directions for every stored friendship. Using `UNION` also protects the logical relation from duplicate directed pairs. Every later step can then reason from the target user to one friend without orientation-specific conditions.

**Generate and filter candidate pages**

Join each directed friendship to `Likes` on `friend_id`. This produces one candidate row for every friend who likes a page; an inner join is important because a friend with no likes contributes no recommendation. Left-join the target user's own likes on both `user_id` and `page_id`, then keep only candidates with no matching own-like row.

**Aggregate friend support**

Group the remaining candidates by target `user_id` and `page_id`. Each source row corresponds to one distinct friend-page like, so `COUNT(*)` is exactly the number of friends supporting that recommendation. Grouping emits each recommendation once.

Every output page has a supporting friend and lacks an own-like match. Conversely, any page satisfying those conditions appears through at least one directed friendship and survives the anti-join, so it is grouped and returned with the exact support count.

#### Complexity detail

Expanding friendships and indexing or hashing the two base relations uses $O(F+L)$ work and storage. The friend-to-like join produces $C$ candidate rows. In a general sort-based plan, deduplication and grouping cost $O((F+L+C)\log C)$ time; hash-based plans can approach linear expected work. Intermediate friendships, join state, candidates, and groups occupy $O(F+L+C)$ space.

#### Alternatives and edge cases

- **One-direction friendship join:** It misses recommendations whenever the target user appears in `user2_id`.
- **Left-join friends to likes:** It can create a spurious recommendation with a null `page_id`; use an inner join for candidate likes.
- **Correlated friend count:** Recounting supporters for every candidate user-page pair is correct but can repeatedly scan the same friendship and like rows.
- **Already-liked page:** Exclude it even if many friends like it.
- **Several supporting friends:** Return one row and count every distinct friend once.
- **One friend liking several pages:** Each not-yet-liked page becomes its own recommendation.
- **Friend with no likes:** That friendship contributes no result row.
- **Isolated liker:** A user with likes but no friendship cannot generate or receive a recommendation.

</details>
