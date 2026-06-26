# Most Visited Sector in  a Circular Track

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1560 |
| Difficulty | Easy |
| Topics | Array, Simulation |
| Official Link | [most-visited-sector-in-a-circular-track](https://leetcode.com/problems/most-visited-sector-in-a-circular-track/) |

## Problem Description & Examples
### Goal
Given a sequence of race checkpoints on a circular track, return the sectors
visited the most often.

### Function Contract
**Inputs**

- `n`: the number of sectors labeled `1` through `n`.
- `rounds`: the visited checkpoint sequence.

**Return value**

The most visited sector labels in increasing order.

### Examples
**Example 1**

- Input: `n = 4, rounds = [1, 3, 1, 2]`
- Output: `[1, 2]`

**Example 2**

- Input: `n = 2, rounds = [2, 1, 2, 1, 2, 1, 2, 1, 2]`
- Output: `[2]`

**Example 3**

- Input: `n = 7, rounds = [1, 3, 5, 7]`
- Output: `[1, 2, 3, 4, 5, 6, 7]`

---

## Underlying Base Algorithm(s)
Only the start and final checkpoint determine which sectors receive one extra
visit after all full laps. If `start <= end`, return every sector from `start`
to `end`; otherwise return `1..end` followed by `start..n`.

---

## Complexity Analysis
- **Time Complexity**: `O(n)` for the output size.
- **Space Complexity**: `O(1)` extra space besides the result.
