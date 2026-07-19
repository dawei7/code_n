# Count Negative Numbers in a Sorted Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1351 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Binary Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/) |

## Problem Description

### Goal

You are given a rectangular integer matrix `grid`. The values in every row are sorted in non-increasing order from left to right, and the values in every column are also sorted in non-increasing order from top to bottom.

Return the total number of entries whose value is strictly less than zero. Zero is not negative. The shared row and column ordering creates a monotone boundary between nonnegative and negative cells, so the entire matrix need not be inspected individually.

### Function Contract

**Inputs**

- `grid`: a nonempty $m \times n$ integer matrix whose rows and columns are each sorted in non-increasing order.
- $m$ and $n$ denote its row and column counts.

**Return value**

- Return the number of cells containing a value less than zero.

### Examples

**Example 1**

- Input: `grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]`
- Output: `8`

**Example 2**

- Input: `grid = [[3,2],[1,0]]`
- Output: `0`

**Example 3**

- Input: `grid = [[1,-1],[-1,-1]]`
- Output: `3`
