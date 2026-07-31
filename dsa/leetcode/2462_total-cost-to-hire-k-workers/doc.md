# Total Cost to Hire K Workers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2462 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Heap (Priority Queue), Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/total-cost-to-hire-k-workers/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `costs`, where `costs[i]` is the price of hiring the worker whose current index is $i$. You must hire exactly `k` workers over `k` sessions, selecting one worker per session. A hired worker is removed and cannot be selected again, so the remaining workers' displayed indices may change.

During a session, consider the first `candidates` remaining workers and the last `candidates` remaining workers. Hire the eligible worker with the lowest cost; if several eligible workers have that cost, choose the one with the smallest current index. When fewer than `candidates` workers remain, all of them are eligible. Return the total cost of the `k` hires.

### Function Contract

**Inputs**

- `costs`: A list in which `costs[i]` is the hiring cost of worker $i$.
- `k`: The exact number of workers to hire.
- `candidates`: The number of remaining workers exposed from each end in a session.

The constraints are $1\le\lvert\texttt{costs}\rvert\le10^5$, $1\le\texttt{costs[i]}\le10^5$, and $1\le k,\texttt{candidates}\le\lvert\texttt{costs}\rvert$.

**Return value**

- The total cost produced by the required sequence of exactly `k` hiring sessions.

### Examples

**Example 1**

- Input: `costs = [17, 12, 10, 2, 7, 2, 11, 20, 8], k = 3, candidates = 4`
- Output: `11`
- Explanation: The selected costs are `2`, `2`, and `7` as the two candidate regions are replenished.

**Example 2**

- Input: `costs = [1, 2, 4, 1], k = 3, candidates = 3`
- Output: `4`
- Explanation: The candidate regions overlap, so each worker is considered only once; the selected costs are `1`, `1`, and `2`.
