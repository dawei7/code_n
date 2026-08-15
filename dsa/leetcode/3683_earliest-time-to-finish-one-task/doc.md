# Earliest Time to Finish One Task

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3683 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/earliest-time-to-finish-one-task/) |

## Problem Description

### Goal

Each row `tasks[i] = [s_i, t_i]` describes an independent task that starts at time $s_i$ and requires $t_i$ time units to complete without interruption. Its finish time is therefore $s_i+t_i$.

Determine the earliest time at which at least one listed task has finished. Tasks do not delay or otherwise interact with one another.

### Function Contract

**Inputs**

- `tasks`: a non-empty list of $n$ two-element rows `[start, duration]`, where $1\le n\le100$ and both values in every row lie from 1 through 100.

**Return value**

Return the minimum completion time `start + duration` among all tasks.

### Examples

#### Example 1

- **Input:** `tasks = [[1, 6], [2, 3]]`
- **Output:** `5`

The tasks finish at times 7 and 5, so the second task finishes first.

#### Example 2

- **Input:** `tasks = [[100, 100], [100, 100], [100, 100]]`
- **Output:** `200`

Every task has the same completion time.

#### Example 3

- **Input:** `tasks = [[10, 20]]`
- **Output:** `30`

With a single task, its finish time is necessarily the answer.
