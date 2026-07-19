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

### Required Complexity

- **Time:** $O(L^2 + F)$
- **Space:** $O(L^2)$

<details>
<summary>Approach</summary>

#### General

**Start from the canonical friend pairs**

Join each `Friendship` row to the listening facts of its first user and then to the facts of its second user. Require the two listening rows to have the same `song_id` and `day`. This prevents nonfriends from ever becoming candidates and retains the stored `user1_id < user2_id` orientation automatically.

**Measure distinct overlap within each day**

Group matching rows by both friend IDs and by `day`. A group represents the songs that one friend pair shared on one particular date. Keep it only when `COUNT(DISTINCT song_id)` is at least three.

The distinct count is necessary because either user's repeated log rows can multiply join matches. Keeping the date in the group is equally necessary because activity from separate dates cannot be accumulated.

**Collapse repeated qualification**

A friendship may satisfy the rule on several days. Applying `DISTINCT` to the projected friend IDs reduces those daily groups to one output row. Every emitted row therefore corresponds to an input friendship with a qualifying day, and every qualifying friendship produces such a group, so the result is exact.

#### Complexity detail

The shared-song join has at most $O(L^2)$ logical row combinations in the worst case, while scanning or indexing the friend relation contributes $O(F)$. Grouping and deduplication remain within $O(L^2)$ intermediate space. Thus the worst-case bounds are $O(L^2+F)$ time and $O(L^2)$ space.

This bound matches the possible output and input scale. With $U$ users, three common songs on one day, and every user pair present in `Friendship`, $L=3U$ and $F=\Theta(U^2)$. Every friendship must be returned, so merely reading and emitting the required relation takes $\Omega(L^2+F)$ work for that family.

#### Alternatives and edge cases

- **Self-join all listeners before checking friendship:** This creates nonfriend candidate pairs unnecessarily; driving from `Friendship` restricts work to the required relation.
- **Group only by friend IDs:** This incorrectly combines common songs heard on different days.
- **Use `COUNT(*)`:** Duplicate listening rows and their join cross-products can falsely reach the threshold.
- **Exactly three distinct songs:** The friendship qualifies because the threshold is inclusive.
- **Multiple qualifying days:** Return the canonical friendship only once.
- **Similar nonfriends:** Exclude the pair even when its listening overlap is otherwise sufficient.
- **Empty listening activity:** No friendship qualifies.

</details>
