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

### Required Complexity

- **Time:** $O(L^2 + F)$
- **Space:** $O(L^2)$

<details>
<summary>Approach</summary>

#### General

**Remove duplicate listening facts first**

Create `DistinctListens` from distinct `(user_id, song_id, day)` triples. This prevents repeated log rows for one song from inflating the common-song threshold.

**Qualify pairs within one day**

Self-join the distinct facts on equal `day` and `song_id`, requiring the first user ID to be smaller than the second. Each joined row represents one distinct song shared by one unordered user pair on one day. Group by both user IDs and `day`, retaining only groups with at least three rows.

Keeping `day` in this grouping is essential: songs shared across different dates cannot be accumulated into one qualifying count. Project the qualifying user IDs with `DISTINCT` afterward so a pair that qualifies on several days is still represented once.

**Exclude friends and emit both directions**

Because candidate pairs are already canonicalized with the smaller user first, one left join to `Friendship` checks the stored orientation exactly. Keep pairs without a friendship row. Emit the canonical direction and its reversal with `UNION ALL`; the two branches are distinct because the user IDs differ.

#### Complexity detail

In the worst case, the self-join can produce $O(L^2)$ shared-listening rows, and grouping those rows uses $O(L^2)$ intermediate state. Friendship exclusion adds $O(F)$ build or lookup work under normal indexed/hash execution. The worst-case time is therefore $O(L^2+F)$ and space is $O(L^2)$.

This bound is output-optimal in the worst case. If $U$ users all listen to the same three songs on one day and none are friends, then $L=3U$ while the required directed output contains $U(U-1)=\Theta(L^2)$ rows.

#### Alternatives and edge cases

- **Group only by user pair:** This is incorrect because common songs from different days can accumulate to three.
- **Count raw `Listens` rows:** Duplicate listening logs can falsely satisfy the distinct-song threshold.
- **Correlated pair subqueries:** Recounting shared songs separately for every user pair repeats work and is harder to optimize.
- **Exactly three songs:** The pair qualifies; the threshold is inclusive.
- **Multiple qualifying days:** Emit each directed recommendation only once.
- **Existing friendship:** Suppress both recommendation directions.
- **Unidirectional output wording:** The relationship is evaluated as an unordered pair, but both directed rows are required.

</details>
