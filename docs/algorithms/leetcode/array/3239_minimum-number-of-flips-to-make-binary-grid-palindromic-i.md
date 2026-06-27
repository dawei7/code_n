# Minimum Number of Flips to Make Binary Grid Palindromic I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3239 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Matrix |
| Official Link | [minimum-number-of-flips-to-make-binary-grid-palindromic-i](https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/) |

## Problem Description & Examples
### Goal
Given a binary matrix, determine the minimum number of bit flips (changing 0 to 1 or vice versa) required to make either all rows palindromic or all columns palindromic. A row or column is palindromic if it reads the same forwards and backwards.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers (a 2D binary matrix).

**Return value**

- An integer representing the minimum flips needed to satisfy the condition for either all rows or all columns.

### Examples
**Example 1**

- Input: `grid = [[1,0,0],[0,0,0],[0,0,1]]`
- Output: `2`

**Example 2**

- Input: `grid = [[0,1],[0,1],[0,0]]`
- Output: `1`

**Example 3**

- Input: `grid = [[1],[0]]`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem relies on the **Two Pointers** technique. For each row (or column), we compare elements at index `i` and `n - 1 - i` moving towards the center. Each mismatch requires exactly one flip to make that specific row (or column) a palindrome. We calculate the total flips required for all rows and all columns independently, then return the minimum of the two sums.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n)`, where `m` is the number of rows and `n` is the number of columns. We iterate through every element in the grid exactly twice (once for row checks, once for column checks).
- **Space Complexity**: `O(1)`, as we only use a few integer variables to track the flip counts, regardless of the input size.
