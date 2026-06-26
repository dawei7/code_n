# Best Team With No Conflicts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1626 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Sorting |
| Official Link | [best-team-with-no-conflicts](https://leetcode.com/problems/best-team-with-no-conflicts/) |

## Problem Description & Examples
### Goal
Select a team with maximum total score such that no younger selected player has
a strictly higher score than an older selected player.

### Function Contract
**Inputs**

- `scores`: player scores.
- `ages`: player ages.

**Return value**

The maximum possible team score.

### Examples
**Example 1**

- Input: `scores = [1, 3, 5, 10, 15], ages = [1, 2, 3, 4, 5]`
- Output: `34`

**Example 2**

- Input: `scores = [4, 5, 6, 5], ages = [2, 1, 2, 1]`
- Output: `16`

**Example 3**

- Input: `scores = [1, 2, 3, 5], ages = [8, 9, 10, 1]`
- Output: `6`

---

## Underlying Base Algorithm(s)
Sort players by age, then by score. After sorting, conflicts are avoided by
choosing a nondecreasing sequence of scores. Run dynamic programming similar to
longest increasing subsequence, where `dp[i]` is the best total score for a team
ending with player `i`.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`.
- **Space Complexity**: `O(n)`.
