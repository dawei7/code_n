# Maximum Value Sum by Placing Three Rooks II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3257 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/) |

## Problem Description

### Goal

The integer matrix \`board\` represents an $m \times n$ chessboard, with each entry giving the value earned by occupying that cell. Place exactly three rooks. Since rooks attack along their row and column, no two selected cells may have the same row index or the same column index.

Maximize and return the sum of the three selected values. Negative entries are legal, so even when every possible placement has a negative total, three cells must still be chosen and that best negative total must be returned.

### Function Contract

**Inputs**

- \`board\`: A rectangular matrix with $3 \le m,n \le 500$ and cell values between $-10^9$ and $10^9$, inclusive.

**Return value**

- The maximum sum of exactly three cells whose rows are pairwise distinct and whose columns are pairwise distinct.

### Examples

**Example 1**

- Input: \`board = [[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]\`
- Output: \`4\`

One optimum uses cells \`(0,2)\`, \`(1,3)\`, and \`(2,1)\`.

**Example 2**

- Input: \`board = [[1,2,3],[4,5,6],[7,8,9]]\`
- Output: \`15\`

Three distinct rows and columns can contribute a maximum total of 15.

**Example 3**

- Input: \`board = [[1,1,1],[1,1,1],[1,1,1]]\`
- Output: \`3\`

All legal placements have equal value.
