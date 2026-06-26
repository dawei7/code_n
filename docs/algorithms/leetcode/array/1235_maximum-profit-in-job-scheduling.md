# Maximum Profit in Job Scheduling

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1235 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Dynamic Programming, Sorting |
| Official Link | [maximum-profit-in-job-scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) |

## Problem Description & Examples
### Goal
Choose a set of non-overlapping jobs to maximize total profit. A job ending at time `t` does not conflict with a job starting at time `t`.

### Function Contract
**Inputs**

- `startTime`: job start times.
- `endTime`: job end times.
- `profit`: job profits at the same indices.

**Return value**

The maximum profit obtainable from compatible jobs.

### Examples
**Example 1**

- Input: `startTime = [1,2,3,3]`, `endTime = [3,4,5,6]`, `profit = [50,10,40,70]`
- Output: `120`

**Example 2**

- Input: `startTime = [1,2,3,4,6]`, `endTime = [3,5,10,6,9]`, `profit = [20,20,100,70,60]`
- Output: `150`

**Example 3**

- Input: `startTime = [1,1,1]`, `endTime = [2,3,4]`, `profit = [5,6,4]`
- Output: `6`

---

## Underlying Base Algorithm(s)
Weighted interval scheduling with binary search.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`
