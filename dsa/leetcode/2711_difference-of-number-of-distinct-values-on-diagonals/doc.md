# Difference of Number of Distinct Values on Diagonals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2711 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/) |

## Problem Description

### Goal

Given an $m \times n$ integer matrix `grid`, construct an equally sized matrix `answer`. For every cell `grid[r][c]`, consider its top-left-to-bottom-right matrix diagonal, which begins in the top row or leftmost column.

Let `leftAbove[r][c]` be the number of distinct values strictly above and to the left of `grid[r][c]` on that diagonal. Let `rightBelow[r][c]` be the number of distinct values strictly below and to the right on the same diagonal. The current cell is excluded from both groups.

Set each result cell to

$$
\texttt{answer[r][c]} =
\left\lvert
\texttt{leftAbove[r][c]} - \texttt{rightBelow[r][c]}
\right\rvert.
$$

Return the completed `answer` matrix.

### Function Contract

**Inputs**

- `grid`: An $m \times n$ matrix of integers.

Here, $m$ is the number of rows and $n$ is the number of columns. The constraints are $1 \le m,n \le 50$ and $1 \le \texttt{grid[i][j]} \le 50$.

**Return value**

- An $m \times n$ integer matrix containing the absolute difference of the two distinct-value counts for every cell.

### Examples

#### Example 1

- **Input:** `grid = [[1,2,3],[3,1,5],[3,2,1]]`
- **Output:** `[[1,1,0],[1,0,1],[0,1,1]]`
- **Explanation:** For the center cell, the value set above-left is `{1}` and the set below-right is also `{1}`, so the difference is $0$. At the top-left cell, the first set is empty while the lower-right set is `{1}`, so the difference is $1$.

#### Example 2

- **Input:** `grid = [[1]]`
- **Output:** `[[0]]`
- **Explanation:** No cells lie above-left or below-right of the only cell, so both distinct counts are zero.
