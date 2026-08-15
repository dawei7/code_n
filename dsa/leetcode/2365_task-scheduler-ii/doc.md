# Task Scheduler II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2365 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/task-scheduler-ii/) |

## Problem Description

### Goal

The positive integers in `tasks` identify task types that must be completed in
their given order. On each day, either complete the next pending task or take
a break; tasks cannot be rearranged.

After completing a task, at least `space` whole days must pass before another
task of the same type can be performed. Return the minimum number of days
needed to finish the entire sequence.

### Function Contract

**Inputs**

- `tasks`: An ordered list of $n$ positive task-type identifiers.
- `space`: The minimum number of intervening days between equal task types.

The constraints are $1\le n\le10^5$, $1\le\texttt{tasks[i]}\le10^9$, and
$1\le\texttt{space}\le n$.

**Return value**

Return the earliest day on which all tasks can be completed. The result may
require a 64-bit integer.

### Examples

#### Example 1

- **Input:** `tasks = [1,2,1,2,3,1], space = 3`
- **Output:** `9`

#### Example 2

- **Input:** `tasks = [5,8,8,5], space = 2`
- **Output:** `6`
