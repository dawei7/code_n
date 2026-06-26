# Search a 2D Matrix II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 240 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Divide and Conquer, Matrix |
| Official Link | [search-a-2d-matrix-ii](https://leetcode.com/problems/search-a-2d-matrix-ii/) |

## Problem Description & Examples
### Goal
Given an $m \times n$ matrix where each row is sorted in ascending order from left to right and each column is sorted in ascending order from top to bottom, determine if a specific target integer exists within the matrix.

### Function Contract
**Inputs**

- `matrix`: A list of lists of integers (`List[List[int]]`) representing the sorted 2D grid.
- `target`: An integer representing the value to search for.

**Return value**

- `bool`: Returns `True` if the target is found in the matrix, otherwise `False`.

### Examples
**Example 1**

- Input: `matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5`
- Output: `True`

**Example 2**

- Input: `matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20`
- Output: `False`

**Example 3**

- Input: `matrix = [[-5]], target = -5`
- Output: `True`

---

## Underlying Base Algorithm(s)
The optimal approach utilizes a "Search Space Reduction" strategy (often called the Staircase Search). By starting at the top-right corner (or bottom-left), we can eliminate an entire row or column in each step. If the current element is greater than the target, the entire column to the right can be ignored. If the current element is less than the target, the entire row above can be ignored.

---

## Complexity Analysis
- **Time Complexity**: $O(m + n)$, where $m$ is the number of rows and $n$ is the number of columns. We traverse at most one row and one column length.
- **Space Complexity**: $O(1)$, as we only use a constant amount of extra space for pointers.
