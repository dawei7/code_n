# Minimum Difficulty of a Job Schedule

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1335 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [minimum-difficulty-of-a-job-schedule](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/) |

## Problem Description & Examples
### Goal
Schedule jobs in their given order over exactly `d` days. Each day must contain at least one job, and a day's difficulty is the maximum job difficulty assigned to that day. Minimize the total difficulty.

### Function Contract
**Inputs**

- `jobDifficulty`: difficulty of each job in fixed order.
- `d`: number of days.

**Return value**

The minimum possible total difficulty, or `-1` if scheduling is impossible.

### Examples
**Example 1**

- Input: `jobDifficulty = [6,5,4,3,2,1]`, `d = 2`
- Output: `7`

**Example 2**

- Input: `jobDifficulty = [9,9,9]`, `d = 4`
- Output: `-1`

**Example 3**

- Input: `jobDifficulty = [1,1,1]`, `d = 3`
- Output: `3`

---

## Underlying Base Algorithm(s)
Dynamic programming over ordered partitions.

---

## Complexity Analysis
- **Time Complexity**: `O(d * n^2)`
- **Space Complexity**: `O(n)`
