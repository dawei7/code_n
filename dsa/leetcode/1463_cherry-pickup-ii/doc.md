# Cherry Pickup II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1463 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/cherry-pickup-ii/) |

## Problem Description
### Goal

A rectangular `grid` represents a field of cherries. The value `grid[i][j]` is the number of cherries available in the cell at row `i` and column `j`. Two robots begin in the top row: robot 1 at the top-left cell `(0, 0)` and robot 2 at the top-right cell `(0, cols - 1)`.

Both robots move simultaneously from one row to the next. From `(i, j)`, a robot may enter `(i + 1, j - 1)`, `(i + 1, j)`, or `(i + 1, j + 1)`, provided that the destination remains inside the grid. Both robots must eventually reach the bottom row, so each robot visits exactly one cell in every row.

When a robot visits a cell, it collects all cherries in that cell. If the robots occupy different cells in a row, both cell values contribute to the total. If they occupy the same cell, that cell is collected only once; the two robots cannot duplicate its cherries. Determine the maximum total number of cherries that the two valid top-to-bottom routes can collect together.

### Function Contract
**Inputs**

- `grid`: an $R \times C$ matrix of integers, where $2 \le R, C \le 70$ and `grid[i][j]` lies between $0$ and $100$, inclusive.
- $R$ is the number of rows and $C$ is the number of columns. Every row has exactly $C$ entries.

**Return value**

Return the maximum combined number of cherries collected by the two robots while both remain in bounds and finish in row $R - 1$.

### Examples
**Example 1**

- Input: `grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]`
- Output: `24`
- Explanation: The robots can collect `3 + 2 + 5 + 2 = 12` and `1 + 5 + 5 + 1 = 12` along two compatible routes.

**Example 2**

- Input: `grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]`
- Output: `28`

**Example 3**

- Input: `grid = [[1,0,1],[0,10,0]]`
- Output: `12`
- Explanation: The robots collect both corner values in the first row. They may then meet on the center cell, whose `10` cherries count once rather than twice.
