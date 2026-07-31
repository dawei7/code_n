# Row With Maximum Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2643 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/row-with-maximum-ones/) |

## Problem Description

### Goal

You are given an $m \times n$ binary matrix `mat`, so every entry is either zero or one. Find the 0-indexed row containing the greatest number of ones and also determine that maximum count.

If several rows contain the same greatest number of ones, select the row with the smallest index. Return both results as `[rowIndex, onesCount]`. Rows are not guaranteed to be sorted, so every entry may affect its row's count.

### Function Contract

**Inputs**

- `mat`: An $m \times n$ binary matrix, where $1 \le m,n \le 100$.

Here, $m$ is the number of rows and $n$ is the number of columns.

**Return value**

- Return `[rowIndex, onesCount]`, choosing the smallest row index among all rows tied for the maximum count.

### Examples

**Example 1**

- Input: `mat = [[0, 1], [1, 0]]`
- Output: `[0, 1]`
- Explanation: Both rows contain one one, so the smaller index wins the tie.

**Example 2**

- Input: `mat = [[0, 0, 0], [0, 1, 1]]`
- Output: `[1, 2]`

**Example 3**

- Input: `mat = [[0, 0], [1, 1], [0, 0]]`
- Output: `[1, 2]`
