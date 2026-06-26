# Maximum Number of Weeks for Which You Can Work

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1953 |
| Difficulty | Medium |
| Topics | Array, Greedy |
| Official Link | [maximum-number-of-weeks-for-which-you-can-work](https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/) |

## Problem Description & Examples
### Goal
Each project has a number of milestones. You may complete one milestone per week, but cannot work on the same project in two consecutive weeks. Maximize the number of weeks worked.

### Function Contract
**Inputs**

- `milestones`: milestone counts for each project.

**Return value**

Return the maximum feasible number of working weeks.

### Examples
**Example 1**

- Input: `milestones = [1,2,3]`
- Output: `6`

**Example 2**

- Input: `milestones = [5,2,1]`
- Output: `7`

**Example 3**

- Input: `milestones = [9,3,3]`
- Output: `15`

---

## Underlying Base Algorithm(s)
Let `largest` be the biggest project and `rest` be all other milestones. If `largest <= rest + 1`, all milestones can be scheduled. Otherwise the dominant project can appear only around the `rest` milestones, giving `2 * rest + 1` weeks.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
