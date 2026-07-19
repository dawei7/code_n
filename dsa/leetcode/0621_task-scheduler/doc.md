# Task Scheduler

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 621 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/task-scheduler/) |

## Problem Description
### Goal
You are given an array of CPU tasks labeled with uppercase letters from `A` through `Z` and a nonnegative integer `n`. Each CPU interval can either complete one task or remain idle, and the tasks may be completed in any order.

Schedule every task using the minimum number of CPU intervals. Between two tasks with the same label, there must be a gap of at least `n` complete intervals, which may contain other tasks or idle time. Count both working and forced-idle intervals in the returned schedule length.

### Function Contract
**Inputs**

- `tasks`: uppercase task identifiers; each list entry is one required execution
- `n`: the nonnegative cooldown between equal task types

**Return value**

- The minimum schedule length, including any forced idle intervals
- Different task types may run in any order

### Examples
**Example 1**

- Input: `tasks = ["A","A","A","B","B","B"]`, `n = 2`
- Output: `8`

**Example 2**

- Input: `tasks = ["A","A","A","B","B","B"]`, `n = 0`
- Output: `6`

**Example 3**

- Input: `tasks = ["A","A","A","B","B","B"]`, `n = 1`
- Output: `6`
