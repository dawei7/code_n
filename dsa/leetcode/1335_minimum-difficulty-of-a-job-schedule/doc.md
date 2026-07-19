# Minimum Difficulty of a Job Schedule

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1335 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/) |

## Problem Description
### Goal
Schedule all jobs represented by `job_difficulty` over exactly `d` days. The jobs are dependent and must be completed in their given order: job $i$ cannot begin until every earlier job has finished. At least one job must be performed on each day, so every day receives one non-empty contiguous segment of the array.

A day's difficulty is the maximum difficulty among the jobs assigned to that day. The total schedule difficulty is the sum of those $d$ daily maxima.

Return the minimum total difficulty obtainable by choosing the $d-1$ boundaries between days. If there are fewer jobs than days, no valid schedule exists and the result is `-1`.

### Function Contract
**Inputs**

- `job_difficulty`: an integer array of length $n$, where $1\le n\le300$ and $0\le\texttt{job_difficulty[i]}\le1000$.
- `d`: the exact number of work days, where $1\le d\le10$.

**Return value**

The minimum sum of daily maximum difficulties for a valid order-preserving schedule, or `-1` when $n<d$.

### Examples
**Example 1**

- Input: `job_difficulty = [6,5,4,3,2,1]`, `d = 2`
- Output: `7`
- Explanation: Assign the first five jobs to day 1 and the last job to day 2, producing $6+1=7$.

**Example 2**

- Input: `job_difficulty = [9,9,9]`, `d = 4`
- Output: `-1`
- Explanation: Four non-empty days cannot be formed from three jobs.

**Example 3**

- Input: `job_difficulty = [1,1,1]`, `d = 3`
- Output: `3`
