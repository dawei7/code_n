# Find Minimum Time to Finish All Jobs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1723 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/) |

## Problem Description

### Goal

Each positive integer in `jobs` is the time required to finish one job. Assign every job to exactly one of `k` workers. A worker may receive any number of jobs, and that worker's working time is the sum of the assigned durations.

For an assignment, consider the largest working time among all workers. Return the minimum possible value of that maximum over every complete assignment of jobs to workers.

### Function Contract

**Inputs**

- `jobs`: an array of $n$ positive durations, where $1 \le n \le 12$ and $1 \le \texttt{jobs[i]} \le 10^7$.
- `k`: the number of workers, with $1 \le k \le n$.

**Return value**

- Return the smallest achievable maximum worker workload.

### Examples

**Example 1**

- Input: `jobs = [3,2,3], k = 3`
- Output: `3`
- Explanation: Assigning one job to each worker makes the largest workload $3$.

**Example 2**

- Input: `jobs = [1,2,4,7,8], k = 2`
- Output: `11`
- Explanation: Workloads $1+2+8=11$ and $4+7=11$ attain the optimum.

**Example 3**

- Input: `jobs = [5,5,4,4,4], k = 2`
- Output: `12`
- Explanation: One worker can receive the two fives while the other receives the three fours.
