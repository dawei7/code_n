# Leetcodify Friends Recommendations

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/leetcodify-friends-recommendations/) |
| Frontend ID | 1917 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

The `Listens` table records songs heard by users on particular dates and may contain duplicate rows. The `Friendship` table stores existing undirected friendships once, with the smaller user ID in `user1_id`.

Two users qualify for a recommendation when they are not already friends and, on at least one single day, both listened to at least three distinct common songs. Return both recommendation directions for every qualifying unordered pair: if users `x` and `y` qualify, emit `(x,y)` and `(y,x)`. Each directed pair must appear only once even if the users qualify on multiple days.

### Function Contract

**Input tables**

- `Listens(user_id, song_id, day)`; duplicate rows are allowed.
- `Friendship(user1_id, user2_id)`; `(user1_id, user2_id)` is the primary key and `user1_id < user2_id`.

Let $L$ be the number of distinct `(user_id, song_id, day)` listening facts and $F$ the number of friendship rows.

**Return value**

- Return columns `user_id` and `recommended_id`.
- Emit both directions of every nonfriend pair sharing at least three distinct songs on the same day.
- Do not emit duplicate directed recommendations. Row order is unrestricted.

### Examples

**Example 1**

- Users `1`, `2`, and `3` each listen to songs `10`, `11`, and `12` on `2021-03-15`; users `1` and `2` are already friends.
- Output: `(1,3)`, `(2,3)`, `(3,1)`, and `(3,2)`.

**Example 2**

- Users `1` and `2` share only songs `10` and `11` on one day.
- Output: no rows.

**Example 3**

- Users `1` and `2` share three songs on two different days.
- Output: only `(1,2)` and `(2,1)`, once each.
