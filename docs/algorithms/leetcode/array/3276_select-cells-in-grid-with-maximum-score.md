# Select Cells in Grid With Maximum Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3276 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Bit Manipulation, Matrix, Bitmask |
| Official Link | [select-cells-in-grid-with-maximum-score](https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/) |

## Problem Description & Examples
### Goal
Given a 2D grid of integers, select a set of cells such that no two cells share the same row. Each selected cell must contain a unique value. The objective is to maximize the sum of the values of the selected cells.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers representing the matrix.

**Return value**

- An integer representing the maximum possible sum of selected cells.

### Examples
**Example 1**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `18`

**Example 2**

- Input: `grid = [[8,7,6],[8,3,1]]`
- Output: `15`

**Example 3**

- Input: `grid = [[1,2,3],[4,5,6]]`
- Output: `9`

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming with Bitmasking. Since we need to select cells with unique values across different rows, we first group the row indices for each unique value present in the grid. We then iterate through the sorted unique values and maintain a bitmask representing the set of rows already occupied. The state `dp[mask]` stores the maximum sum achievable using a subset of rows represented by the bitmask.

---

## Complexity Analysis
- **Time Complexity**: `O(V * 2^R)`, where `V` is the number of unique values in the grid and `R` is the number of rows. In the worst case, this is efficient enough given the constraints on grid dimensions.
- **Space Complexity**: `O(2^R)` to store the DP table for all possible row combinations.
