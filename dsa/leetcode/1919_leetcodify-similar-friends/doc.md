# Leetcodify Similar Friends

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/leetcodify-similar-friends/) |
| Frontend ID | 1919 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

The `Listens` table records which song each user heard on each date and may contain duplicate rows. The `Friendship` table records every friendship once, placing the smaller user ID in `user1_id`.

Report the existing friend pairs whose listening activity is similar: on at least one single day, both users must have listened to three or more distinct songs in common. Return each qualifying pair once in the same canonical orientation used by `Friendship`. Sharing songs without being friends does not qualify, and songs from different days cannot be combined toward the threshold.

### Function Contract

**Input tables**

- `Listens(user_id, song_id, day)`; duplicate rows are allowed.
- `Friendship(user1_id, user2_id)`; `(user1_id, user2_id)` is the primary key and `user1_id < user2_id`.

Let $L$ be the number of distinct `(user_id, song_id, day)` listening facts and $F$ the number of friendship rows.

**Return value**

- Return columns `user1_id` and `user2_id`.
- Include an existing friendship when its users share at least three distinct songs on one day.
- Preserve `user1_id < user2_id`, emit each friendship at most once, and use any row order.

### Examples

**Example 1**

- Friends `1` and `2` both listen to songs `10`, `11`, and `12` on `2021-03-15`.
- Output: `(1,2)`.

Users `1` and `3` may have identical activity, but their pair is excluded when they are not friends.

**Example 2**

- Friends `2` and `4` share only songs `10` and `11` on one day.
- Output: no rows.

**Example 3**

- Friends `2` and `5` share three songs, but user `2` hears them on a different date from user `5`.
- Output: no rows.
