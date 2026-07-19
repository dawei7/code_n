# Page Recommendations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1264 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/page-recommendations/) |

## Problem Description

### Goal

The `Friendship` table stores undirected friendships as two user identifiers, and `Likes` records which pages each user likes. A friendship involving user `1` may place that user in either friendship column.

Recommend every page liked by at least one friend of user `1` that user `1` has not already liked. Return each recommended page only once even when several friends like it. Pages liked only by nonfriends must not appear, and the result may be returned in any order.

### Function Contract

**Inputs**

- `Friendship(user1_id, user2_id)`: unique undirected friendship pairs.
- `Likes(user_id, page_id)`: unique user-page likes.
- Let $F$ and $L$ be the two table row counts, and let $R=F+L$.

**Return value**

- Return one column named `recommended_page` containing the distinct eligible page identifiers for user `1`.

### Examples

**Example 1**

If users `2`, `3`, `4`, and `6` are friends of user `1`, their liked pages are candidates regardless of which friendship column contains `1`. A page already liked by user `1` is excluded, while a page shared by users `2` and `3` appears once.

**Example 2**

When every page liked by a friend is also liked by user `1`, the result is empty.

**Example 3**

A page liked by a user with no friendship edge to user `1` is not recommended.
