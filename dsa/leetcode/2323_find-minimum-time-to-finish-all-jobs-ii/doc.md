# Find Minimum Time to Finish All Jobs II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2323 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/) |

## Problem Description

### Goal

Two equally long arrays describe jobs and workers. `jobs[i]` is the total amount of work required by one job, while `workers[j]` is the amount of that work a particular worker can complete per day.

Assign every job to exactly one worker and every worker to exactly one job. A worker assigned work amount $a$ at daily capacity $b$ finishes after $\lceil a/b \rceil$ days. All assignments proceed concurrently, so the completion time is the largest individual duration. Return the smallest possible number of days over all one-to-one assignments.

### Function Contract

**Inputs**

- `jobs`: A list of positive job workloads.
- `workers`: An equally long list of positive daily worker capacities.

The common length $n$ is between $1$ and $10^5$. Every workload and capacity is between $1$ and $10^5$.

**Return value**

Return the minimum integer number of days after which every job can be complete under an optimal one-to-one assignment.

### Examples

**Example 1**

- Input: `jobs = [5,2,4], workers = [1,7,5]`
- Output: `2`

Pairing sorted workloads `[2,4,5]` with sorted capacities `[1,5,7]` produces durations 2, 1, and 1 day.

**Example 2**

- Input: `jobs = [3,18,15,9], workers = [6,5,1,3]`
- Output: `3`

The sorted pairs finish in at most three days, and no assignment can make every pair finish sooner.
