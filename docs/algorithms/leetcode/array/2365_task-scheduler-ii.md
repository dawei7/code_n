# Task Scheduler II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2365 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Simulation |
| Official Link | [task-scheduler-ii](https://leetcode.com/problems/task-scheduler-ii/) |

## Problem Description & Examples
### Goal
Given a sequence of tasks represented by integers and a cooldown period `space`, determine the minimum number of days required to complete all tasks in the given order. You must wait at least `space` days between executing two tasks of the same type.

### Function Contract
**Inputs**

- `tasks`: A list of integers where each integer represents a specific task type.
- `space`: An integer representing the minimum number of days that must pass between executing two tasks of the same type.

**Return value**

- An integer representing the total number of days elapsed to complete all tasks.

### Examples
**Example 1**

- Input: `tasks = [1,2,1,2,3,1], space = 3`
- Output: `9`
- Explanation: Day 1: Task 1, Day 2: Task 2, Day 3: Idle, Day 4: Idle, Day 5: Task 1, Day 6: Task 2, Day 7: Task 3, Day 8: Idle, Day 9: Task 1.

**Example 2**

- Input: `tasks = [5,8,8,5], space = 2`
- Output: `6`
- Explanation: Day 1: Task 5, Day 2: Task 8, Day 3: Idle, Day 4: Idle, Day 5: Task 8, Day 6: Task 5.

**Example 3**

- Input: `tasks = [1,2,3], space = 1`
- Output: `3`

---

## Underlying Base Algorithm(s)
The problem is solved using a Greedy Simulation approach combined with a Hash Map (Dictionary). We maintain a record of the last day each task type was performed. For each task in the sequence, we calculate the earliest possible day it can be executed based on the `space` constraint and the last recorded execution day. If the current day is earlier than the required day, we advance the current day to the required day.

---

## Complexity Analysis
- **Time Complexity**: O(N), where N is the number of tasks, as we iterate through the list exactly once.
- **Space Complexity**: O(K), where K is the number of unique task types, to store the last execution day for each task in a hash map.
