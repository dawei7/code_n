# Difference Between Ones and Zeros in Row and Column

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2482 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/) |

## Problem Description

### Goal

Given a zero-indexed $m \times n$ binary matrix `grid`, construct another $m \times n$ matrix `diff`.

For cell `(i, j)`, count the ones and zeros in row `i` and in column `j`. Set `diff[i][j]` to the row's number of ones plus the column's number of ones, minus the row's number of zeros and the column's number of zeros.

Return the complete difference matrix. Every cell in the same row shares the row contribution, and every cell in the same column shares the column contribution.

### Function Contract

**Inputs**

- `grid`: A nonempty rectangular matrix containing only `0` and `1`.

Let $m = \lvert\texttt{grid}\rvert$ and $n = \lvert\texttt{grid[0]}\rvert$. The constraints satisfy $1 \le m,n \le 10^5$ and $1 \le mn \le 10^5$.

**Return value**

Return an $m \times n$ integer matrix where

$$
\texttt{diff[i][j]} = \texttt{onesRow}_i + \texttt{onesCol}_j - \texttt{zerosRow}_i - \texttt{zerosCol}_j.
$$

### Examples

**Example 1**

- Input: `grid = [[0,1,1],[1,0,1],[0,0,1]]`
- Output: `[[0,0,4],[0,0,4],[-2,-2,2]]`
- Explanation: The row one-counts are `[2,2,1]` and the column one-counts are `[1,1,3]`.

**Example 2**

- Input: `grid = [[1,1,1],[1,1,1]]`
- Output: `[[5,5,5],[5,5,5]]`
- Explanation: Each row contributes three more ones than zeros and each column contributes two more ones than zeros.

**Example 3**

- Input: `grid = [[0]]`
- Output: `[[-2]]`
- Explanation: The only row and column each contribute one more zero than one.
