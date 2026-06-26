# Minimum Total Distance Traveled

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2463 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Sorting |
| Official Link | [minimum-total-distance-traveled](https://leetcode.com/problems/minimum-total-distance-traveled/) |

## Problem Description & Examples
### Goal
Given a set of robot positions on a 1D line and a set of factory locations, each with a specific repair capacity, assign each robot to a factory such that every robot is repaired and the total distance traveled by all robots is minimized. Each factory can only repair a limited number of robots.

### Function Contract
**Inputs**

- `robot`: A list of integers representing the 1D coordinates of each robot.
- `factory`: A list of lists, where each inner list `[position, limit]` represents the coordinate of a factory and the maximum number of robots it can repair.

**Return value**

- An integer representing the minimum total distance all robots must travel to reach their assigned factories.

### Examples
**Example 1**

- Input: `robot = [0,4,6], factory = [[2,2],[6,2]]`
- Output: `4`

**Example 2**

- Input: `robot = [1,-1], factory = [[-2,1],[2,1]]`
- Output: `2`

**Example 3**

- Input: `robot = [1,2,3], factory = [[1,1],[2,1],[3,1]]`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming. First, sort both the robots and the factories by their positions. We define `dp[i][j]` as the minimum cost to repair the first `i` robots using a subset of the first `j` factories. The transition involves deciding how many robots (from 0 up to the factory's limit) the `j`-th factory will repair.

---

## Complexity Analysis
- **Time Complexity**: `O(N * M * K)`, where `N` is the number of robots, `M` is the number of factories, and `K` is the maximum capacity of a factory. Given the constraints, this is efficient enough.
- **Space Complexity**: `O(N * M)` to store the DP table.
