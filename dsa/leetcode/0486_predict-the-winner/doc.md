# Predict the Winner

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 486 |
| Difficulty | Medium |
| Topics | Array, Math, Dynamic Programming, Recursion, Game Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/predict-the-winner/) |

## Problem Description
### Goal
Two players begin with score zero and alternately take one number from either end of the nonempty array `nums`, with player 1 moving first. The chosen number is added to that player's score and removed, and the game ends after every number has been taken.

Assuming both players play optimally, return whether player 1 can finish with a score greater than or equal to player 2's score. A tie therefore counts as a player-1 win. Each decision may change which values become available at the two ends, so the result concerns a guaranteed strategy rather than a greedy choice of the larger visible endpoint.

### Function Contract
**Inputs**

- `nums`: a nonempty array of nonnegative scores

**Return value**

- `True` if the first player can force a win or tie; otherwise `False`

### Examples
**Example 1**

- Input: `nums = [1, 5, 2]`
- Output: `False`

**Example 2**

- Input: `nums = [1, 5, 233, 7]`
- Output: `True`

**Example 3**

- Input: `nums = [1, 1]`
- Output: `True`
