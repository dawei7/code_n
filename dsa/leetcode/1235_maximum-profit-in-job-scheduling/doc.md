# Maximum Profit in Job Scheduling

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1235 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) |

## Problem Description

### Goal

There are $n$ jobs. Job $i$ runs from `start_time[i]` until `end_time[i]` and earns `profit[i]` when selected. Choose any subset of the jobs, but do not choose two jobs whose time ranges overlap.

A job ending at time $X$ is compatible with another job starting at exactly time $X$; their shared endpoint is not an overlap. Return the maximum total profit obtainable from a compatible subset. Jobs need not be presented in chronological order, and selecting no unnecessary job does not incur a penalty.

### Function Contract

**Inputs**

- `start_time`: A list of $n$ job start times, where $1\le n\le5\cdot10^4$.
- `end_time`: A list of the corresponding end times, with $1\le\texttt{start_time[i]}<\texttt{end_time[i]}\le10^9$.
- `profit`: A list of corresponding positive profits, where $1\le\texttt{profit[i]}\le10^4$.

**Return value**

- The maximum sum of profits from jobs whose time ranges do not overlap.

### Examples

**Example 1**

- Input: `start_time = [1,2,3,3]`, `end_time = [3,4,5,6]`, `profit = [50,10,40,70]`
- Output: `120`

The jobs `[1,3]` and `[3,6]` touch at time $3$ and earn $50+70=120$.

**Example 2**

- Input: `start_time = [1,2,3,4,6]`, `end_time = [3,5,10,6,9]`, `profit = [20,20,100,70,60]`
- Output: `150`

Selecting `[1,3]`, `[4,6]`, and `[6,9]` earns $20+70+60=150$.

**Example 3**

- Input: `start_time = [1,1,1]`, `end_time = [2,3,4]`, `profit = [5,6,4]`
- Output: `6`

Every pair overlaps, so the single job worth $6$ is optimal.
