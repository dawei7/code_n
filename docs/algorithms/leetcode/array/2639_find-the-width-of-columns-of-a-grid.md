# Find the Width of Columns of a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2639 |
| Difficulty | Easy |
| Topics | Array, Matrix |
| Official Link | [find-the-width-of-columns-of-a-grid](https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/) |

## Problem Description & Examples
### Goal
Given a 2D integer matrix, determine the maximum character width of each column. The width of a column is defined as the number of digits in the longest integer within that column, accounting for the negative sign if the integer is negative.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers (`List[List[int]]`) representing the matrix.

**Return value**

- A list of integers (`List[int]`) where the $i$-th element represents the maximum width found in the $i$-th column of the grid.

### Examples
**Example 1**

- Input: `grid = [[1],[22],[333]]`
- Output: `[3]`

**Example 2**

- Input: `grid = [[-15,1,3],[15,7,12]]`
- Output: `[3,1,2]`

**Example 3**

- Input: `grid = [[0]]`
- Output: `[1]`

---

## Underlying Base Algorithm(s)
The problem is solved using a linear scan approach. We iterate through each column index, and for every column, we iterate through all rows to find the string representation length of each integer. We maintain a running maximum for each column index.

---

## Complexity Analysis
- **Time Complexity**: $O(m \times n)$, where $m$ is the number of rows and $n$ is the number of columns, as we must visit every element in the grid exactly once.
- **Space Complexity**: $O(n)$ to store the result list containing the maximum width for each of the $n$ columns.
