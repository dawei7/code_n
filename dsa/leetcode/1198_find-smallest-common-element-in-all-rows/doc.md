# Find Smallest Common Element in All Rows

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1198 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Matrix, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-smallest-common-element-in-all-rows/) |

## Problem Description

### Goal

You are given an $m\times n$ integer matrix `mat`. Every row is sorted in strictly increasing order, so a value occurs at most once within any individual row even though it may occur in several different rows.

Find the smallest value that appears in every row of the matrix. Return that value when one or more common elements exist; return `-1` when the rows have no element shared by all of them.

### Function Contract

**Inputs**

- `mat`: An $m\times n$ matrix, where $1\le m,n\le500$ and $1\le\texttt{mat[i][j]}\le10^4$.
- Every row `mat[i]` is sorted in strictly increasing order.

**Return value**

- The smallest integer present in all $m$ rows, or `-1` if no such integer exists.

### Examples

**Example 1**

- Input: `mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]`
- Output: `5`

The value `5` occurs in all four rows.

**Example 2**

- Input: `mat = [[1,2,3],[2,3,4],[2,3,5]]`
- Output: `2`

Both `2` and `3` are common, and `2` is smaller.

**Example 3**

- Input: `mat = [[1,2,3],[4,5,6]]`
- Output: `-1`
