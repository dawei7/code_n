# Minimum Time to Complete All Tasks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2589 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Stack, Greedy, Sorting |
| Official Link | [minimum-time-to-complete-all-tasks](https://leetcode.com/problems/minimum-time-to-complete-all-tasks/) |

## Problem Description & Examples
### Goal
Given a list of tasks where each task specifies a start time, an end time, and a required duration, determine the minimum number of time units (points) that must be active to satisfy all task requirements. A task is completed if it is active for its required duration within its specified [start, end] interval.

### Function Contract
**Inputs**

- `tasks`: A list of lists, where each inner list `[start, end, duration]` represents a task that must be completed within the inclusive range `[start, end]` for a total of `duration` time units.

**Return value**

- An integer representing the minimum number of time units that need to be marked as "active" to satisfy all task requirements.

### Examples
**Example 1**

- Input: `tasks = [[2,3,1],[4,5,1],[1,5,2]]`
- Output: `2`

**Example 2**

- Input: `tasks = [[1,3,2],[2,5,3],[5,6,2]]`
- Output: `4`

**Example 3**

- Input: `tasks = [[1,3,2],[4,9,3],[10,10,1]]`
- Output: `6`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy approach with Sorting**. By sorting the tasks based on their end times, we can process tasks that finish earlier first. We maintain a boolean array (or a set of active time points) to track which time units are already "active." For each task, we count how many time units are already active within its interval. If the count is less than the required duration, we greedily fill the remaining required time units starting from the end of the interval moving backwards, as these points are most likely to be useful for subsequent tasks.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N + N * M)`, where `N` is the number of tasks and `M` is the maximum end time. Sorting takes `O(N log N)`, and for each task, we iterate through its time range.
- **Space Complexity**: `O(M)`, where `M` is the maximum end time, used to store the status of each time unit.
