# Find the Minimum Area to Cover All Ones I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3195 |
| Difficulty | Medium |
| Topics | Array, Matrix |
| Official Link | [find-the-minimum-area-to-cover-all-ones-i](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/) |

## Problem Description & Examples
### Goal
Given a 2D binary grid containing zeros and ones, determine the area of the smallest axis-aligned rectangle that encompasses every cell containing a one.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers (a 2D matrix) where each element is either 0 or 1.

**Return value**

- An integer representing the area (width × height) of the smallest rectangle that contains all ones present in the grid.

### Examples
**Example 1**

- Input: `grid = [[0,1,0],[1,0,1]]`
- Output: `6`
- Explanation: The ones are at (0,1), (1,0), and (1,2). The bounding box spans rows 0 to 1 and columns 0 to 2. Height = 2, Width = 3, Area = 6.

**Example 2**

- Input: `grid = [[1,0],[0,0]]`
- Output: `1`
- Explanation: The only one is at (0,0). The bounding box is 1x1, Area = 1.

**Example 3**

- Input: `grid = [[0,0],[1,0]]`
- Output: `1`
- Explanation: The only one is at (1,0). The bounding box is 1x1, Area = 1.

---

## Underlying Base Algorithm(s)
The problem is solved by finding the bounding box coordinates: the minimum and maximum row indices (`min_r`, `max_r`) and the minimum and maximum column indices (`min_c`, `max_c`) among all cells containing a 1. The area is then calculated as `(max_r - min_r + 1) * (max_c - min_c + 1)`.

---

## Complexity Analysis
- **Time Complexity**: `O(R * C)`, where R is the number of rows and C is the number of columns, as we must iterate through every cell in the grid once.
- **Space Complexity**: `O(1)`, as we only store four integer variables to track the boundaries.
