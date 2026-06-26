# Find Minimum Time to Finish All Jobs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1723 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Official Link | [find-minimum-time-to-finish-all-jobs](https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/) |

## Problem Description & Examples
### Goal
Assign every job to one of `k` workers. A worker's time is the sum of assigned job durations, and the overall workload is the maximum worker time. Minimize that maximum.

### Function Contract
**Inputs**

- `jobs`: a list of positive job durations.
- `k`: the number of workers.

**Return value**

Return the smallest possible maximum worker workload.

### Examples
**Example 1**

- Input: `jobs = [3,2,3], k = 3`
- Output: `3`

**Example 2**

- Input: `jobs = [1,2,4,7,8], k = 2`
- Output: `11`

**Example 3**

- Input: `jobs = [5,5,4,4,4], k = 2`
- Output: `12`

---

## Underlying Base Algorithm(s)
A common optimal approach is binary search on the answer. For a candidate limit, use backtracking to try assigning jobs, usually sorted descending, to workers without any worker exceeding the limit. Prune symmetric empty workers and duplicate load states. The first feasible limit is optimal.

---

## Complexity Analysis
- **Time Complexity**: `O(log S * k^n)` worst case with strong pruning in practice
- **Space Complexity**: `O(k + n)`
