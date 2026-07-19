# Minimum Number of Work Sessions to Finish the Tasks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1986 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/) |

## Problem Description
### Goal
You must complete `n` tasks whose durations are listed in `tasks`. Work is
divided into sessions, each lasting at most `sessionTime` hours before a break.
Once a task starts, it must finish within that same session; tasks cannot be
split across breaks, although multiple tasks may be completed consecutively in
one session.

The tasks may be performed in any order. Assign every task to a session without
exceeding the per-session time limit, and return the minimum number of sessions
needed. Every individual task is guaranteed to fit within one session.

### Function Contract
**Inputs**

- `tasks`: a list of $N$ positive task durations, where $1 \le N \le 14$ and
  $1 \le \texttt{tasks[i]} \le 10$.
- `sessionTime`: the capacity $S$ of each session, where
  $\max(\texttt{tasks}) \le S \le 15$.

**Return value**

- The minimum number of capacity-$S$ sessions that can contain all tasks,
  assigning each task wholly to exactly one session.

### Examples
**Example 1**

- Input: `tasks = [1, 2, 3], sessionTime = 3`
- Output: `2`

Tasks `1` and `2` share one session, while task `3` uses another.

**Example 2**

- Input: `tasks = [3, 1, 3, 1, 1], sessionTime = 8`
- Output: `2`

Four tasks totaling `8` can share the first session.

**Example 3**

- Input: `tasks = [1, 2, 3, 4, 5], sessionTime = 15`
- Output: `1`
