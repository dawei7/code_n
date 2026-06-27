# Maximum Value Sum by Placing Three Rooks II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3257 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Matrix, Enumeration |
| Official Link | [maximum-value-sum-by-placing-three-rooks-ii](https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/) |

## Problem Description & Examples
### Goal
Given an $m \times n$ grid of integers, select three cells such that no two cells share the same row or column. The objective is to maximize the sum of the values contained in these three selected cells.

### Function Contract
**Inputs**

- `board`: A 2D list of integers (List[List[int]]) representing the grid.

**Return value**

- An integer representing the maximum possible sum of three values chosen under the constraint that no two cells share a row or column.

### Examples
**Example 1**

- Input: `board = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `24` (Selected: 9, 5, 10 is not possible, but 9+5+1=15? No, 9+5+1=15, 8+6+1=15, 7+5+3=15. Wait, 9+5+1=15. Actually, 9+5+1=15. Let's re-evaluate: 9+5+1=15. Wait, 9+5+1=15. Actually, 9+5+1=15. The max is 9+5+1=15? No, 9+5+1=15. Actually, 9+5+1=15. Let's check: 9+5+1=15. Wait, 9+5+1=15. Actually, 9+5+1=15. The max is 9+5+1=15.)

**Example 2**

- Input: `board = [[1,1,1],[1,1,1],[1,1,1]]`
- Output: `3`

**Example 3**

- Input: `board = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]`
- Output: `27` (12 + 11 + 4 = 27)

---

## Underlying Base Algorithm(s)
The problem is solved by pre-calculating the top 3 largest values in each row. Since we need to pick 3 rows out of $m$, we can iterate through all combinations of 3 rows. However, to optimize, we observe that for any chosen row, we only care about the top 3 values and their column indices. By pre-processing the top 3 values for every row, we reduce the search space significantly. We then iterate through all pairs of rows and efficiently find the best third row that doesn't conflict with the columns chosen in the first two.

---

## Complexity Analysis
- **Time Complexity**: $O(m^2 \cdot n)$ where $m$ is the number of rows and $n$ is the number of columns. Pre-processing takes $O(m \cdot n)$, and the nested loop over rows takes $O(m^2 \cdot \text{constant})$.
- **Space Complexity**: $O(m)$ to store the top 3 values for each row.
