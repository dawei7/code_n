# Find the Grid of Region Average

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3030 |
| Difficulty | Medium |
| Topics | Array, Matrix |
| Official Link | [find-the-grid-of-region-average](https://leetcode.com/problems/find-the-grid-of-region-average/) |

## Problem Description & Examples
### Goal
Given a 2D grid of integers and a threshold value, identify all 3x3 subgrids where the intensity difference between any two adjacent cells (horizontally or vertically) does not exceed the threshold. For such "valid" regions, calculate the integer average of the 9 cells. The output is a grid of the same dimensions where each cell contains the average of all valid 3x3 regions it belongs to, or the original value if it belongs to no valid regions.

### Function Contract
**Inputs**

- `grid`: A 2D list of integers of size `m x n`.
- `threshold`: An integer representing the maximum allowed absolute difference between adjacent cells in a valid region.

**Return value**

- A 2D list of integers of size `m x n` representing the processed grid.

### Examples
**Example 1**

- Input: `grid = [[5,6,7],[8,9,10],[11,12,13]], threshold = 1`
- Output: `[[9,9,9],[9,9,9],[9,9,9]]`

**Example 2**

- Input: `grid = [[10,20,30],[15,25,35],[50,60,70]], threshold = 200`
- Output: `[[34,34,34],[34,34,34],[34,34,34]]`

**Example 3**

- Input: `grid = [[10],[20],[30]], threshold = 1`
- Output: `[[10],[20],[30]]`

---

## Underlying Base Algorithm(s)
The solution utilizes a sliding window approach over the 2D grid. For every possible top-left corner `(i, j)` of a 3x3 subgrid, we perform a local validation check by iterating through the 9 cells and verifying the adjacency threshold condition. We maintain a secondary data structure to store the sum of averages and a count of how many valid regions cover each cell, allowing us to compute the final result in a single pass.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n)`, where `m` and `n` are the dimensions of the grid. We iterate through the grid once to identify regions and once to compute the final averages.
- **Space Complexity**: `O(m * n)` to store the auxiliary grids for region sums and counts.
