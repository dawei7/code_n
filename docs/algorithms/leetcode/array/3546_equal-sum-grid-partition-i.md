# Equal Sum Grid Partition I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3546 |
| Difficulty | Medium |
| Topics | Array, Matrix, Enumeration, Prefix Sum |
| Official Link | [equal-sum-grid-partition-i](https://leetcode.com/problems/equal-sum-grid-partition-i/) |

## Problem Description & Examples
### Goal
Given a 2D grid of integers, determine if it is possible to partition the grid into four rectangular sub-grids by drawing one horizontal line and one vertical line. The goal is to check if there exists a configuration where the sum of elements in each of the four resulting quadrants is equal.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers representing the 2D matrix.

**Return value**

- `bool`: Returns `True` if there exists a horizontal cut at row `i` and a vertical cut at column `j` such that the four resulting rectangular regions have identical sums, otherwise `False`.

### Examples
**Example 1**

- Input: `grid = [[1, 2], [3, 4]]`
- Output: `False`

**Example 2**

- Input: `grid = [[1, 1], [1, 1]]`
- Output: `True`

**Example 3**

- Input: `grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
- Output: `False`

---

## Underlying Base Algorithm(s)
The problem is solved using 2D Prefix Sums (or Summed-Area Table). By precomputing the prefix sums, we can calculate the sum of any rectangular sub-grid in $O(1)$ time. We then iterate through all possible horizontal cut positions (between rows) and vertical cut positions (between columns), checking if the four resulting quadrants have equal sums.

---

## Complexity Analysis
- **Time Complexity**: $O(M \times N)$, where $M$ is the number of rows and $N$ is the number of columns. We perform a single pass to build the prefix sum table and a nested loop to check all possible cut combinations.
- **Space Complexity**: $O(M \times N)$ to store the 2D prefix sum table.
