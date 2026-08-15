# Zigzag Grid Traversal With Skip

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3417 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/zigzag-grid-traversal-with-skip/) |

## Problem Description

### Goal

Traverse a rectangular grid in zigzag row order. Start at the top-left cell and move left to right across the first row. Drop to the second row and move right to left, then continue alternating direction for each following row until the grid has been traversed.

During that single traversal, visit the first cell, skip the next, visit the next, and continue skipping every alternate cell globally. The visit/skip phase does not restart at a row boundary. Return the values of the visited cells in traversal order.

### Function Contract

**Inputs**

- `grid`: A rectangular matrix of positive integers.

Let $m=\lvert\texttt{grid}\rvert$ and $n=\lvert\texttt{grid[0]}\rvert$. The constraints are $2\le m,n\le50$ and $1\le\texttt{grid[i][j]}\le2500$.

**Return value**

- A list containing every other value in the zigzag traversal, beginning with `grid[0][0]`.

### Examples

#### Example 1

- **Input:** `grid = [[1, 2], [3, 4]]`
- **Output:** `[1, 4]`

The zigzag order is `[1, 2, 4, 3]`; taking positions 0 and 2 gives `[1, 4]`.

#### Example 2

- **Input:** `grid = [[2, 1], [2, 1], [2, 1]]`
- **Output:** `[2, 1, 2]`

#### Example 3

- **Input:** `grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
- **Output:** `[1, 3, 5, 7, 9]`

The odd row width changes which columns are visited in the next row, demonstrating that skipping continues across row boundaries.
