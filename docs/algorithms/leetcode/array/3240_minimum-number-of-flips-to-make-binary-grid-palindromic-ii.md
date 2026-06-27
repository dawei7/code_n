# Minimum Number of Flips to Make Binary Grid Palindromic II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3240 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Matrix |
| Official Link | [minimum-number-of-flips-to-make-binary-grid-palindromic-ii](https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/) |

## Problem Description & Examples
### Goal
Given a binary matrix, determine the minimum number of bit flips (changing 0 to 1 or 1 to 0) required to make the grid palindromic in both row-wise and column-wise directions, with the additional constraint that the total number of 1s in the grid must be divisible by 4.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers (a 2D binary matrix).

**Return value**

- An integer representing the minimum number of flips required to satisfy the palindrome and parity constraints.

### Examples
**Example 1**

- Input: `grid = [[1,0,0],[0,1,0],[0,0,1]]`
- Output: `3`

**Example 2**

- Input: `grid = [[0,1],[0,1],[0,0]]`
- Output: `2`

**Example 3**

- Input: `grid = [[1],[1]]`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem is solved by partitioning the grid into groups of 4 symmetric cells (e.g., `(r, c)`, `(r, n-1-c)`, `(m-1-r, c)`, `(m-1-r, n-1-c)`). For each group, we calculate the cost to make all bits equal and track the number of 1s. Special handling is required for the middle row/column (if dimensions are odd) where groups consist of only 2 cells, and the absolute center (if both dimensions are odd) which is a single cell. We use a greedy approach combined with a parity check to ensure the total count of 1s is a multiple of 4.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n)`, where `m` is the number of rows and `n` is the number of columns, as we iterate through the grid once.
- **Space Complexity**: `O(1)`, as we only use a few variables to track counts and costs regardless of input size.
