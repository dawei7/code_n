# Coin Path

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 656 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/coin-path/) |

## Problem Description
### Goal
Given an array `coins`, start at its first position and try to reach its final position by jumping forward at most `maxJump` indices at a time. A nonnegative entry is the cost paid when that position is visited, while `-1` marks a blocked position on which you may not land.

Among all valid paths, minimize the sum of the visited position costs, including the start and destination. If several paths have the same minimum cost, return the lexicographically smallest sequence of one-based indices. Return an empty list when the last position cannot be reached, including when an endpoint is blocked.

### Function Contract
**Inputs**

- `coins`: a nonempty list where a nonnegative value is the cost of visiting that position and `-1` marks a blocked position
- `maxJump`: the positive maximum distance of one forward jump

**Return value**

- The lexicographically smallest minimum-cost path as 1-based indices, or `[]` when the last position is unreachable

### Examples
**Example 1**

- Input: `coins = [1, 2, 4, -1, 2]`, `maxJump = 2`
- Output: `[1, 3, 5]`

**Example 2**

- Input: `coins = [1, 2, 4, -1, 2]`, `maxJump = 1`
- Output: `[]`

**Example 3**

- Input: `coins = [1, 1, 1, 1]`, `maxJump = 2`
- Output: `[1, 2, 4]`
