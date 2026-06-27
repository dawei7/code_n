# Minimum Processing Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2895 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [minimum-processing-time](https://leetcode.com/problems/minimum-processing-time/) |

## Problem Description & Examples
### Goal
Given a list of processor start times and a list of tasks with varying execution durations, assign each processor exactly four tasks. The goal is to minimize the total time required to complete all tasks, where the completion time for a specific processor is defined as its start time plus the duration of the longest task assigned to it. The total time is the maximum completion time among all processors.

### Function Contract
**Inputs**

- `processorTime`: A list of integers representing the time at which each processor becomes available.
- `tasks`: A list of integers representing the duration of each task.

**Return value**

- An integer representing the minimum possible time required to finish all tasks.

### Examples
**Example 1**

- Input: `processorTime = [8, 10]`, `tasks = [2, 2, 3, 1, 8, 7, 4, 5]`
- Output: `16`

**Example 2**

- Input: `processorTime = [10, 20]`, `tasks = [2, 3, 1, 2, 5, 8, 4, 3]`
- Output: `23`

**Example 3**

- Input: `processorTime = [1, 5]`, `tasks = [1, 1, 1, 1, 1, 1, 1, 1]`
- Output: `6`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy Strategy**. To minimize the maximum completion time, we should pair the processors that become available latest with the tasks that take the longest time. By sorting the `processorTime` in descending order and the `tasks` in ascending order, we can greedily assign the four largest tasks to the processor that starts latest, the next four largest to the next latest, and so on.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N + M log M)`, where `N` is the number of processors and `M` is the number of tasks. This is dominated by the sorting of both input arrays.
- **Space Complexity**: `O(1)` or `O(N + M)` depending on the sorting implementation's space requirements.
