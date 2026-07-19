# Minimum Initial Energy to Finish Tasks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1665 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/) |

## Problem Description
### Goal
Each task is described by `[actual, minimum]`. You must have at least `minimum` energy immediately before starting that task, and completing it permanently consumes `actual` energy. For example, a `[10, 12]` task cannot start from 11 energy; starting from 13 leaves 3 afterward.

All tasks must be completed, but their order is yours to choose. Determine the smallest initial energy for which some ordering satisfies every start threshold and energy cost.

### Function Contract
**Inputs**

- `tasks`: an array of $n$ pairs `[actual, minimum]`, where $1 \le n \le 10^5$ and $1 \le \texttt{actual} \le \texttt{minimum} \le 10^4$.

**Return value**

Return the minimum initial energy that permits completion of every task in an optimally chosen order.

### Examples
**Example 1**

- Input: `tasks = [[1, 2], [2, 4], [4, 8]]`
- Output: `8`

Ordering the tasks as `[4, 8]`, `[2, 4]`, `[1, 2]` succeeds from 8.

**Example 2**

- Input: `tasks = [[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]]`
- Output: `32`

**Example 3**

- Input: `tasks = [[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]]`
- Output: `27`
