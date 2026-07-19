# Low-Quality Problems

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2026 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/low-quality-problems/) |

## Problem Description

### Goal

The `Problems` table records the numbers of likes and dislikes received by
each problem. A problem is considered low quality when its likes form strictly
less than 60% of all votes cast for it.

Return the identifiers of every low-quality problem, ordered by `problem_id`
in ascending order. A problem whose like percentage is exactly 60% does not
qualify. The result contains no vote-count columns.

### Function Contract

Let $P$ be the number of rows in `Problems`.

**Inputs**

- `Problems(problem_id, likes, dislikes)`, where `problem_id` is the primary
  key and the other columns contain the vote counts.

**Return value**

- A table with one column, `problem_id`, containing qualifying identifiers in
  ascending order.

### Examples

**Example 1**

- Input: problems `1`, `6`, `7`, `10`, `11`, and `13` with their supplied
  like and dislike counts
- Output: problem IDs `7`, `10`, `11`, and `13`
- Explanation: Each returned problem has a like percentage below 60%; problems
  `1` and `6` are above the threshold.

**Example 2**

- Input: one problem with `likes = 3` and `dislikes = 2`
- Output: no rows
- Explanation: Its like percentage is exactly 60%, not strictly below it.

**Example 3**

- Input: problem `9` with one like and nine dislikes
- Output: problem ID `9`
