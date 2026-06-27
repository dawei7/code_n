# Right Triangles

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3128 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Combinatorics, Counting |
| Official Link | [right-triangles](https://leetcode.com/problems/right-triangles/) |

## Problem Description & Examples
### Goal
Given a binary grid, identify all possible right-angled triangles whose vertices are located at cells containing a `1`. A triangle is valid if its vertices are at `(r1, c1)`, `(r1, c2)`, and `(r2, c1)`, where `r1 != r2` and `c1 != c2`. The goal is to count the total number of such triangles that can be formed.

### Function Contract
**Inputs**

- `grid`: A 2D list of integers (0 or 1) representing the binary matrix.

**Return value**

- An integer representing the total count of valid right-angled triangles.

### Examples
**Example 1**

- Input: `grid = [[0,1,0],[0,1,1],[0,1,0]]`
- Output: `2`

**Example 2**

- Input: `grid = [[1,0,0],[0,1,0],[0,0,1]]`
- Output: `0`

**Example 3**

- Input: `grid = [[1,0,1],[1,0,0],[1,0,0]]`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem is solved using a combinatorial counting approach. For every cell `(i, j)` containing a `1`, it can serve as the corner where the right angle is formed. To form a triangle, we need one other `1` in the same row `i` and one other `1` in the same column `j`. If there are `R_i` ones in row `i` and `C_j` ones in column `j`, the number of triangles with the right angle at `(i, j)` is `(R_i - 1) * (C_j - 1)`. We pre-calculate the sum of ones for each row and column to achieve efficient lookups.

---

## Complexity Analysis
- **Time Complexity**: `O(M * N)`, where `M` is the number of rows and `N` is the number of columns, as we iterate through the grid twice (once for pre-calculation and once for counting).
- **Space Complexity**: `O(M + N)` to store the counts of ones for each row and column.
