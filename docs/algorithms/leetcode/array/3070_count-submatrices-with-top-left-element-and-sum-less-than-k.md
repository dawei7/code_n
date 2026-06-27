# Count Submatrices with Top-Left Element and Sum Less Than k

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3070 |
| Difficulty | Medium |
| Topics | Array, Matrix, Prefix Sum |
| Official Link | [count-submatrices-with-top-left-element-and-sum-less-than-k](https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/) |

## Problem Description & Examples
### Goal
Given a 2D grid of non-negative integers and an integer `k`, determine the total number of submatrices that start at the top-left corner (0, 0) and have a total sum of elements strictly less than `k`.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers representing the 2D matrix.
- `k`: An integer representing the threshold sum.

**Return value**

- An integer representing the count of submatrices starting at (0, 0) with a sum less than `k`.

### Examples
**Example 1**

- Input: `grid = [[7,6,3],[6,6,1]], k = 18`
- Output: `4`

**Example 2**

- Input: `grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20`
- Output: `6`

---

## Underlying Base Algorithm(s)
The problem is solved using 2D Prefix Sums. By precomputing a prefix sum matrix where each cell `(i, j)` stores the sum of the rectangle from `(0, 0)` to `(i, j)`, we can determine the sum of any submatrix starting at `(0, 0)` in constant time. The algorithm iterates through every cell in the grid, calculates the prefix sum, and increments a counter if the sum is less than `k`.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n)`, where `m` is the number of rows and `n` is the number of columns, as we traverse the grid once to compute prefix sums.
- **Space Complexity**: `O(m * n)` to store the prefix sum matrix (or `O(1)` if modifying the input grid in-place).
