# Last Day Where You Can Still Cross

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1970 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/last-day-where-you-can-still-cross/) |

## Problem Description
### Goal
A 1-based binary matrix has `row` rows and `col` columns. Every cell is land
on day `0`. Thereafter, exactly one new cell becomes water per day according
to the permutation `cells`: entry `cells[i]` gives the 1-based row and column
flooded on day `i + 1`.

On a given day, crossing is possible when a path of land cells starts anywhere
in the top row, ends anywhere in the bottom row, and moves only up, down, left,
or right. Return the latest day number on which such a top-to-bottom path still
exists.

### Function Contract
**Inputs**

- `row`: the number of matrix rows, where $2 \le \texttt{row} \le 2\cdot10^4$.
- `col`: the number of matrix columns, where
  $2 \le \texttt{col} \le 2\cdot10^4$.
- `cells`: all $N=\texttt{row}\cdot\texttt{col}$ distinct matrix coordinates
  in their flooding order, with $4 \le N \le 2\cdot10^4$.

**Return value**

- The greatest day in the range from `0` through `N` for which a land-only
  top-to-bottom crossing exists after that day's flooding.

### Examples
**Example 1**

- Input: `row = 2, col = 2, cells = [[1, 1], [2, 1], [1, 2], [2, 2]]`
- Output: `2`

**Example 2**

- Input: `row = 2, col = 2, cells = [[1, 1], [1, 2], [2, 1], [2, 2]]`
- Output: `1`

**Example 3**

- Input: `row = 3, col = 3, cells = [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]`
- Output: `3`
