# Maximum Performance of a Team

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1383 |
| Difficulty | Hard |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue) |
| Official Link | [maximum-performance-of-a-team](https://leetcode.com/problems/maximum-performance-of-a-team/) |

## Problem Description & Examples
### Goal
Choose at most `k` engineers. The team's performance is the sum of chosen speeds multiplied by the minimum efficiency among the chosen engineers. Return the largest possible performance value.

### Function Contract
**Inputs**

- `n`: the number of engineers.
- `speed`: a list of each engineer's speed.
- `efficiency`: a list of each engineer's efficiency.
- `k`: the maximum team size.

**Return value**

The maximum performance, returned modulo `1_000_000_007` when required by the platform contract.

### Examples
**Example 1**

- Input: `n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2`
- Output: `60`

**Example 2**

- Input: `n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3`
- Output: `68`

**Example 3**

- Input: `n = 3, speed = [5,5,5], efficiency = [1,2,3], k = 1`
- Output: `15`

---

## Underlying Base Algorithm(s)
Greedy sorting with a min-heap. Process engineers from highest to lowest efficiency so the current engineer's efficiency is the team's minimum, keep the largest `k` speeds seen so far, and test each candidate performance.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n + n log k)`
- **Space Complexity**: `O(n + k)`
