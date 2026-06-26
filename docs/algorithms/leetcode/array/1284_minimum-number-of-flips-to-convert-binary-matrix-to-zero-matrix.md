# Minimum Number of Flips to Convert Binary Matrix to Zero Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1284 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Bit Manipulation, Breadth-First Search, Matrix |
| Official Link | [minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix](https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/) |

## Problem Description & Examples
### Goal
Each move chooses one cell and toggles that cell plus its four orthogonal neighbors if present. Find the fewest moves needed to turn the whole binary matrix into zeroes.

### Function Contract
**Inputs**

- `mat`: an `m x n` binary matrix.

**Return value**

The minimum number of flips required, or `-1` if the zero matrix is unreachable.

### Examples
**Example 1**

- Input: `mat = [[0,0],[0,1]]`
- Output: `3`

**Example 2**

- Input: `mat = [[0]]`
- Output: `0`

**Example 3**

- Input: `mat = [[1,1,1],[1,0,1],[0,0,0]]`
- Output: `6`

---

## Underlying Base Algorithm(s)
Bitmask state encoding and breadth-first search.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n * 2^(m*n))`
- **Space Complexity**: `O(2^(m*n))`
