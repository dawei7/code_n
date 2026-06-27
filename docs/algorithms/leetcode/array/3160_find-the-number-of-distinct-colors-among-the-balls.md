# Find the Number of Distinct Colors Among the Balls

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3160 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Simulation |
| Official Link | [find-the-number-of-distinct-colors-among-the-balls](https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/) |

## Problem Description & Examples
### Goal
Given a sequence of queries where each query assigns a specific color to a ball at a given index, track the total number of unique colors currently present on the balls after each assignment. If a ball already has a color, it is overwritten by the new one.

### Function Contract
**Inputs**

- `limit`: An integer representing the maximum index of a ball (balls are indexed from 0 to `limit`).
- `queries`: A list of lists, where each inner list `[ball, color]` represents an update operation.

**Return value**

- A list of integers where the $i$-th element is the count of distinct colors present on the balls after the $i$-th query.

### Examples
**Example 1**

- Input: `limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]`
- Output: `[1, 2, 2, 3]`

**Example 2**

- Input: `limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]`
- Output: `[1, 2, 2, 3, 4]`

**Example 3**

- Input: `limit = 1, queries = [[0,1],[0,4],[1,2],[1,2],[0,3]]`
- Output: `[1, 1, 2, 2, 3]`

---

## Underlying Base Algorithm(s)
The problem is solved using a simulation approach supported by two Hash Maps (dictionaries in Python). One map tracks the current color of each ball (`ball_to_color`), and the other tracks the frequency of each color currently in use (`color_counts`). This allows for $O(1)$ updates and lookups per query.

---

## Complexity Analysis
- **Time Complexity**: $O(Q)$, where $Q$ is the number of queries, as each query involves constant-time dictionary operations.
- **Space Complexity**: $O(Q + L)$, where $Q$ is the number of queries and $L$ is the number of balls, to store the mappings of balls to colors and the counts of each color.
