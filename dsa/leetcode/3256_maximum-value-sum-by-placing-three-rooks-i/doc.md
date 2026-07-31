# Maximum Value Sum by Placing Three Rooks I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3256 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/) |

## Problem Description

### Goal

An $m \times n$ chessboard assigns an integer value to every cell \`board[i][j]\`. Place exactly three rooks on cells of the board. Two rooks attack each other when they share a row or a column, so all three chosen row indices must be distinct and all three chosen column indices must also be distinct.

Return the maximum possible sum of the three occupied cell values. Values may be negative, and three rooks must still be placed; the answer is therefore not implicitly bounded below by zero.

### Function Contract

**Inputs**

- \`board\`: A rectangular matrix with $3 \le m,n \le 100$ and $-10^9 \le \texttt{board[i][j]} \le 10^9$.

**Return value**

- The greatest sum obtainable from exactly three cells in pairwise distinct rows and columns.

### Examples

**Example 1**

- Input: \`board = [[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]\`
- Output: \`4\`

Cells \`(0,2)\`, \`(1,3)\`, and \`(2,1)\` contribute $1+1+2$.

**Example 2**

- Input: \`board = [[1,2,3],[4,5,6],[7,8,9]]\`
- Output: \`15\`

Every legal placement uses all three rows and columns; the best sum is 15.

**Example 3**

- Input: \`board = [[1,1,1],[1,1,1],[1,1,1]]\`
- Output: \`3\`

Any three cells in distinct rows and columns achieve the same sum.
