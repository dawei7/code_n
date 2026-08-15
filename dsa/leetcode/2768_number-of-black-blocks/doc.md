# Number of Black Blocks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2768 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [2768. Number of Black Blocks](https://leetcode.com/problems/number-of-black-blocks/) |

## Problem Description

### Goal

Consider a 0-indexed grid with `m` rows and `n` columns. Every cell is initially white except for the pairwise distinct positions listed in `coordinates`, which are black. The dimensions can be very large even though the number of listed black cells is comparatively small.

A block is any contiguous $2 \times 2$ submatrix. Its top-left position $(r,c)$ satisfies $0 \le r < m-1$ and $0 \le c < n-1$, and the block contains the four cells at offsets $(0,0)$, $(1,0)$, $(0,1)$, and $(1,1)$. Return five counts: entry $i$ must equal the number of blocks containing exactly $i$ black cells, for every $i$ from $0$ through $4$.

### Function Contract

**Inputs**

- `m`: The number of grid rows, with $2 \le m \le 10^5$.
- `n`: The number of grid columns, with $2 \le n \le 10^5$.
- `coordinates`: A list of pairwise distinct `[row, column]` positions of black cells. Every position lies within the grid, and the list contains at most $10^4$ entries.

Let $k = \lvert\texttt{coordinates}\rvert$.

**Return value**

Return an integer list `answer` of length $5$, where `answer[i]` is the number of $2 \times 2$ blocks containing exactly $i$ black cells.

### Examples

#### Example 1

- **Input:** `m = 3, n = 3, coordinates = [[0, 0]]`
- **Output:** `[3, 1, 0, 0, 0]`
- **Explanation:** The black corner belongs only to the block whose top-left cell is `[0, 0]`; the other three blocks contain no black cells.

#### Example 2

- **Input:** `m = 3, n = 3, coordinates = [[0, 0], [1, 1], [0, 2]]`
- **Output:** `[0, 2, 2, 0, 0]`
- **Explanation:** Two blocks contain one black cell and the other two contain two black cells.
