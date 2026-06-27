# Find the Minimum Area to Cover All Ones II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3197 |
| Difficulty | Hard |
| Topics | Array, Matrix, Enumeration |
| Official Link | [find-the-minimum-area-to-cover-all-ones-ii](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/) |

## Problem Description & Examples
### Goal
Given a binary matrix, determine the minimum total area required to cover all '1's in the grid using exactly three non-overlapping rectangles. The rectangles must be axis-aligned and can be placed anywhere as long as they cover all existing '1's in the matrix.

### Function Contract
**Inputs**

- `grid`: A 2D list of integers (0 or 1) representing the binary matrix.

**Return value**

- An integer representing the minimum combined area of three rectangles that cover all '1's.

### Examples
**Example 1**

- Input: `grid = [[0,1,0],[1,0,1]]`
- Output: `6`

**Example 2**

- Input: `grid = [[1,0,1,0],[0,1,0,1]]`
- Output: `5`

---

## Underlying Base Algorithm(s)
The problem is solved by partitioning the grid into three regions using two cuts. There are two primary ways to partition the grid:
1. **Three parallel cuts**: Either three horizontal cuts or three vertical cuts.
2. **One cut followed by a perpendicular cut**: One horizontal cut splitting the grid into two, then one of those halves is split by a vertical cut (or vice versa).

For any defined sub-rectangle, the minimum area to cover all '1's is the area of the bounding box of all '1's contained within that sub-rectangle. We iterate through all possible cut positions to find the minimum sum of areas.

## Complexity Analysis
- **Time Complexity**: $O(M \cdot N \cdot (M + N))$, where $M$ is the number of rows and $N$ is the number of columns. We iterate through all possible cut combinations, and calculating the bounding box takes $O(M \cdot N)$.
- **Space Complexity**: $O(M \cdot N)$ to store the grid and potentially $O(1)$ auxiliary space if we optimize bounding box calculations.
