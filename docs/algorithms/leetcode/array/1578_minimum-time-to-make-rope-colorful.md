# Minimum Time to Make Rope Colorful

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1578 |
| Difficulty | Medium |
| Topics | Array, String, Dynamic Programming, Greedy |
| Official Link | [minimum-time-to-make-rope-colorful](https://leetcode.com/problems/minimum-time-to-make-rope-colorful/) |

## Problem Description & Examples
### Goal
Remove balloons so no two adjacent balloons have the same color, minimizing the
total removal time.

### Function Contract
**Inputs**

- `colors`: a string of balloon colors.
- `neededTime`: removal time for each corresponding balloon.

**Return value**

The minimum total time needed to make adjacent colors different.

### Examples
**Example 1**

- Input: `colors = "abaac", neededTime = [1, 2, 3, 4, 5]`
- Output: `3`

**Example 2**

- Input: `colors = "abc", neededTime = [1, 2, 3]`
- Output: `0`

**Example 3**

- Input: `colors = "aabaa", neededTime = [1, 2, 3, 4, 1]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Process each maximal group of equal adjacent colors. Within a group, all but one
balloon must be removed, so pay the group's total time minus its largest single
removal time.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(1)`.
