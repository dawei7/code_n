# Largest 1-Bordered Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1139 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/largest-1-bordered-square/) |

## Problem Description

### Goal

You are given a two-dimensional `grid` whose entries are `0` or `1`. A square subgrid is 1-bordered when every cell along its top, bottom, left, and right edges contains `1`; cells strictly inside the border may contain either value.

Find the largest such square and return its number of elements, which is the square of its side length. A single cell containing `1` is a valid square of area `1`. If the grid contains no 1-bordered square at all, return `0`.

### Function Contract

**Inputs**

- `grid`: an $m \times n$ binary matrix, where $1 \le m,n \le 100$.
- Every `grid[row][column]` is either `0` or `1`.

Let $q=\min(m,n)$.

**Return value**

The area of the largest square subgrid whose complete border consists of `1`s, or `0` if none exists.

### Examples

**Example 1**

- Input: `grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]`
- Output: `9`
- Explanation: The outer border is all `1`, so the entire $3 \times 3$ grid qualifies despite its zero center.

**Example 2**

- Input: `grid = [[1, 1, 0, 0]]`
- Output: `1`
- Explanation: A one-row grid cannot contain a square with side greater than one, but each `1` is a valid side-one square.
