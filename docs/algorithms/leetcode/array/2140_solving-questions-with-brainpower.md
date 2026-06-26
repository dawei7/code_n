# Solving Questions With Brainpower

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2140 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [solving-questions-with-brainpower](https://leetcode.com/problems/solving-questions-with-brainpower/) |

## Problem Description & Examples
### Goal
Choose questions from left to right to maximize earned points. Solving question `i` earns its points but forces the next `brainpower[i]` questions to be skipped; skipping a question has no such restriction.

### Function Contract
**Inputs**

- `questions`: pairs `[points, brainpower]` in their given order.

**Return value**

The maximum total points obtainable.

### Examples
**Example 1**

- Input: `questions = [[3, 2], [4, 3], [4, 4], [2, 5]]`
- Output: `5`

**Example 2**

- Input: `questions = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]`
- Output: `7`

**Example 3**

- Input: `questions = [[10, 0]]`
- Output: `10`

---

## Underlying Base Algorithm(s)
Use dynamic programming from right to left. At index `i`, compare skipping to `dp[i + 1]` with solving for `points[i] + dp[min(n, i + brainpower[i] + 1)]`. Store the larger value.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
