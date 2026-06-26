# Maximum Number of Robots Within Budget

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2398 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Queue, Sliding Window, Heap (Priority Queue), Prefix Sum, Monotonic Queue |
| Official Link | [maximum-number-of-robots-within-budget](https://leetcode.com/problems/maximum-number-of-robots-within-budget/) |

## Problem Description & Examples
### Goal
Given two arrays representing the running costs and charging costs of robots, determine the maximum number of consecutive robots you can select such that the total cost—defined as the maximum charging cost in the selection plus the sum of running costs multiplied by the number of robots—does not exceed a specified budget.

### Function Contract
**Inputs**

- `chargeTimes`: A list of integers representing the charging cost of each robot.
- `runningCosts`: A list of integers representing the running cost of each robot.
- `budget`: A long integer representing the maximum allowed total cost.

**Return value**

- An integer representing the maximum length of a contiguous subarray of robots that satisfies the budget constraint.

### Examples
**Example 1**

- Input: `chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25`
- Output: `3`

**Example 2**

- Input: `chargeTimes = [11,12,19], runningCosts = [10,8,7], budget = 19`
- Output: `0`

**Example 3**

- Input: `chargeTimes = [8,7,6,1], runningCosts = [8,2,5,1], budget = 32`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Sliding Window** technique combined with a **Monotonic Queue** (specifically a deque). The monotonic queue maintains the indices of the maximum charging costs within the current window in $O(1)$ amortized time. A prefix sum array or a running sum variable is used to track the total running costs efficiently.

---

## Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the number of robots. Each element is added and removed from the deque at most once.
- **Space Complexity**: $O(n)$ in the worst case for the deque storing indices.
