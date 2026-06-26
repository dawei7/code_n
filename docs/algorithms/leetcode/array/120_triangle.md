# Triangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 120 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [triangle](https://leetcode.com/problems/triangle/) |

## Problem Description & Examples
### Goal
Given a triangular array, find the minimum path sum from the top to the bottom. Each move may go to the same index or the next index in the row below.

### Function Contract
**Inputs**

- `triangle`: list of rows forming a number triangle.

**Return value**

The minimum total along a valid top-to-bottom path.

### Examples
**Example 1**

- Input: `triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]`
- Output: `11`

**Example 2**

- Input: `triangle = [[-10]]`
- Output: `-10`

**Example 3**

- Input: `triangle = [[1],[2,3],[4,5,6]]`
- Output: `7`

---

## Underlying Base Algorithm(s)
Bottom-up dynamic programming.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)` for all cells in the triangle.
- **Space Complexity**: `O(n)` where `n` is the bottom row length.
