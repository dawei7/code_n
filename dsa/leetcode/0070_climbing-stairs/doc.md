# Climbing Stairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 70 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/climbing-stairs/) |

## Problem Description
### Goal
A staircase has `n` steps, and each move may climb either one step or two steps. Starting below the first step, form movement sequences whose step sizes total exactly `n` without passing the top.

Return the number of distinct valid sequences. Order matters: for a three-step staircase, $1 + 2$ and $2 + 1$ are different ways. The input lies from `1` through `45`, so every staircase has at least one route consisting entirely of one-step moves.

### Function Contract
**Inputs**

- `n`: the positive number of stairs, with $1 \le n \le 45$

**Return value**

The number of valid move sequences.

### Examples
**Example 1**

- Input: `n = 2`
- Output: `2`

**Example 2**

- Input: `n = 3`
- Output: `3`

**Example 3**

- Input: `n = 5`
- Output: `8`
