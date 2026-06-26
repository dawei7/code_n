# Escape the Spreading Fire

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2258 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Breadth-First Search, Matrix |
| Official Link | [escape-the-spreading-fire](https://leetcode.com/problems/escape-the-spreading-fire/) |

## Problem Description & Examples
### Goal
Starting at the top-left cell, wait for some number of minutes and then move one cell per minute to reach the bottom-right safehouse while fire spreads simultaneously through non-wall cells. Entering a cell at the same time as fire is forbidden except at the safehouse. Find the longest safe initial wait.

### Function Contract
**Inputs**

- `grid`: `0` for grass, `1` for initial fire, and `2` for a wall.

**Return value**

The maximum safe waiting time; `-1` if escape is impossible even immediately, or `1_000_000_000` if waiting indefinitely remains safe.

### Examples
**Example 1**

- Input: `grid = [[0, 0], [0, 0]]`
- Output: `1_000_000_000`

**Example 2**

- Input: `grid = [[0, 1], [0, 0]]`
- Output: `-1`

**Example 3**

- Input: `grid = [[0, 0, 0], [0, 2, 0], [1, 2, 0]]`
- Output: `1`

---

## Underlying Base Algorithm(s)
Run multi-source BFS from all initial fires to record their earliest arrival at every reachable cell. Binary-search the initial waiting time. For each candidate, BFS the person's path with absolute arrival times: every ordinary cell requires arrival strictly before fire, while the safehouse permits arrival at the same time. If a wait of at least the grid-cell bound works, fire can never force failure and the required sentinel is returned.

---

## Complexity Analysis
- **Time Complexity**: `O(mn log(mn))`
- **Space Complexity**: `O(mn)`
