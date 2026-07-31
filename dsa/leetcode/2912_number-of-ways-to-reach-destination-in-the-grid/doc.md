# Number of Ways to Reach Destination in the Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2912 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-reach-destination-in-the-grid/) |

## Problem Description

### Goal

Consider an $n$-by-$m$ grid whose rows and columns are numbered from one. The
arrays `source` and `dest` each identify one cell as `[row, column]`. During one
move, you may choose any different cell in the current cell's row or any
different cell in its column. Remaining at the current cell is not a move.

Count the distinct sequences of cells that start at `source`, finish at `dest`,
and contain exactly $k$ moves. A route that reaches the destination early is
counted only if its later moves return to the destination at step $k$. Return
the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `n`: The number of grid rows, with $2\le n\le 10^9$.
- `m`: The number of grid columns, with $2\le m\le 10^9$.
- `k`: The exact number of moves, with $1\le k\le 10^5$.
- `source`: A two-element array `[row, column]` identifying the starting cell.
- `dest`: A two-element array `[row, column]` identifying the destination cell.

Both coordinates are one-indexed and lie within the grid.

**Return value**

Return the number of valid exactly-$k$-move routes from `source` to `dest`,
reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `n = 3, m = 2, k = 2, source = [1, 1], dest = [2, 2]`
- Output: `2`
- Explanation: The two routes use `[1, 2]` or `[2, 1]` as their intermediate cell.

**Example 2**

- Input: `n = 3, m = 4, k = 3, source = [1, 2], dest = [2, 3]`
- Output: `9`

**Example 3**

- Input: `n = 3, m = 4, k = 2, source = [2, 3], dest = [2, 3]`
- Output: `5`
- Explanation: The route must leave and return; there are three other cells in the row and two in the column.
