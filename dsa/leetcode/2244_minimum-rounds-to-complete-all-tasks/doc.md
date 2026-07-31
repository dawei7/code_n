# Minimum Rounds to Complete All Tasks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2244 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/) |

## Problem Description

### Goal

Each value in the 0-indexed array `tasks` is the difficulty level of one task.
During a round, you must complete either two or three tasks, and every task
chosen for that round must have the same difficulty level. Tasks with
different difficulty values therefore cannot share a round.

Complete every task using the fewest possible rounds. Return that minimum
number, or return `-1` when the available multiplicities make completion
impossible.

### Function Contract

**Inputs**

- `tasks`: An array of $n$ task difficulty values, where $1\le n\le10^5$ and $1\le\texttt{tasks[i]}\le10^9$.

**Return value**

Return the minimum number of rounds that partition all tasks into same-
difficulty groups of size two or three, or `-1` if no such partition exists.

### Examples

**Example 1**

- Input: `tasks = [2,2,3,3,2,4,4,4,4,4]`
- Output: `4`

**Example 2**

- Input: `tasks = [2,3,3]`
- Output: `-1`

**Example 3**

- Input: `tasks = [7,7,7,7]`
- Output: `2`
