# Candy Crush

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 723 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Matrix, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/candy-crush/) |

## Problem Description
### Goal
Given a board of candy types, identify every horizontal or vertical run containing at least three equal candies. During one round, crush all candies belonging to any qualifying run simultaneously, including candies that participate in both a horizontal and vertical run.

After the crush, let the remaining candies in each column fall downward and fill vacated cells above them with zeroes. Repeat detection, simultaneous crushing, and gravity until the board is stable and no qualifying run remains. Return that final board; do not let one marked removal hide another run from the same round.

### Function Contract
**Inputs**

- `board`: a rectangular integer matrix in which positive values identify candy types and zero represents an empty cell

**Return value**

- The stable board after all simultaneous crush-and-gravity rounds, with empty cells above the remaining candies in each column

### Examples
**Example 1**

- Input: `board = [[1,1,1],[2,3,4],[5,6,7]]`
- Output: `[[0,0,0],[2,3,4],[5,6,7]]`

**Example 2**

- Input: `board = [[1,2,1],[2,1,2],[1,2,1]]`
- Output: `[[1,2,1],[2,1,2],[1,2,1]]`

**Example 3**

- Input: `board = [[1,2,1],[2,2,2],[1,2,1]]`
- Output: `[[0,0,0],[1,0,1],[1,0,1]]`
