# Maximum Side Length of a Square with Sum Less than or Equal to Threshold

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1292 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Matrix, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/) |

## Problem Description
### Goal
Given an $m \times n$ matrix `mat` of nonnegative integers and an integer `threshold`, consider every contiguous square submatrix and the sum of all values inside it. A candidate square must use the same number of consecutive rows and consecutive columns.

Return the maximum side length among squares whose sum is less than or equal to `threshold`. Return zero when no one-cell square satisfies the limit; otherwise return the largest feasible positive length.

### Function Contract
**Inputs**

- `mat`: an $m \times n$ matrix, where $1 \le m,n \le 300$ and $0 \le \texttt{mat[r][c]} \le 10^4$.
- `threshold`: an integer satisfying $0 \le \texttt{threshold} \le 10^5$.

**Return value**

The largest integer $s$ for which at least one $s \times s$ submatrix has sum at most `threshold`, or zero if no positive side length is valid.

### Examples
**Example 1**

- Input: `mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]`, `threshold = 4`
- Output: `2`

**Example 2**

- Input: `mat = [[2,2],[2,2]]`, `threshold = 1`
- Output: `0`

**Example 3**

- Input: `mat = [[1,0,1],[0,1,0],[1,0,1]]`, `threshold = 2`
- Output: `2`
