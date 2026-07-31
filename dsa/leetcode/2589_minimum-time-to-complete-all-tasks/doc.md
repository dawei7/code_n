# Minimum Time to Complete All Tasks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2589 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Stack, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-to-complete-all-tasks/) |

## Problem Description

### Goal

A computer can run any number of tasks simultaneously. Each `tasks[i] = [start_i, end_i, duration_i]` requires the computer to be on for a total of `duration_i` integer seconds inside the inclusive interval `[start_i, end_i]`. Those seconds need not be consecutive.

Whenever the computer is on, that same second contributes to every task whose interval contains it. The computer may be turned off at all other times, so overlapping tasks can share selected seconds without additional cost.

Choose the on/off schedule that completes every task and return the minimum total number of seconds for which the computer is on.

### Function Contract

**Inputs**

- `tasks`: A list of $n$ triples `[start_i, end_i, duration_i]`, where $1 \leq n \leq 2000$, $1 \leq \texttt{start_i}, \texttt{end_i} \leq 2000$, and $1 \leq \texttt{duration_i} \leq \texttt{end_i} - \texttt{start_i} + 1$.

Let $T$ be the largest `end_i`, and let $N=n+T$ denote the combined task-and-timeline workload.

**Return value**

- The minimum number of distinct integer seconds at which the computer must be on.

### Examples

**Example 1**

- Input: `tasks = [[2,3,1],[4,5,1],[1,5,2]]`
- Output: `2`

Turning the computer on at seconds `2` and `5` satisfies all three tasks.

**Example 2**

- Input: `tasks = [[1,3,2],[2,5,3],[5,6,2]]`
- Output: `4`

One minimum schedule uses seconds `2`, `3`, `5`, and `6`.
