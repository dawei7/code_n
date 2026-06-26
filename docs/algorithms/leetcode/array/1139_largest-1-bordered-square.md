# Largest 1-Bordered Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1139 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [largest-1-bordered-square](https://leetcode.com/problems/largest-1-bordered-square/) |

## Problem Description & Examples
### Goal
Find the area of the largest square in a binary grid whose four borders are all `1`. Cells inside the square may be either `0` or `1`.

### Function Contract
**Inputs**

- `grid`: an `m x n` matrix of `0` and `1`.

**Return value**

The area of the largest square with a border made entirely of `1`s, or `0` if no such square exists.

### Examples
**Example 1**

- Input: `grid = [[1,1,1],[1,0,1],[1,1,1]]`
- Output: `9`

**Example 2**

- Input: `grid = [[1,1,0,0]]`
- Output: `1`

**Example 3**

- Input: `grid = [[0,0],[0,0]]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Dynamic programming for directional run lengths.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n * min(m, n))`
- **Space Complexity**: `O(m * n)`
