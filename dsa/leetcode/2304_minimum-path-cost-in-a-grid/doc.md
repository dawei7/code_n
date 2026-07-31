# Minimum Path Cost in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2304 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-path-cost-in-a-grid/) |

## Problem Description
### Goal
The $m\times n$ matrix `grid` contains every distinct integer from $0$ through
$mn-1$. A path may start in any first-row cell. From a cell in any nonfinal
row, it may move to any column of the next row; a last-row cell has no outgoing
move.

Moving from a cell whose value is `v` into column `c` costs
`moveCost[v][c]`. A complete path's cost includes every visited cell value as
well as every transition cost. Find the minimum total among all paths that
begin in the first row and end in the last row.

### Function Contract
**Inputs**

- `grid`: An $m\times n$ matrix containing each value from $0$ through $mn-1$
  exactly once.
- `moveCost`: An $(mn)\times n$ matrix where row `v` gives the costs of moving
  from value `v` to each next-row column.

The dimensions satisfy $2\le m,n\le50$, and every move cost is from 1 through
100. Entries for moves out of the last row are present but irrelevant.

**Return value**

The minimum sum of visited values and transition costs over a first-to-last-row
path.

### Examples
**Example 1**

- Input: `grid = [[5, 3], [4, 0], [2, 1]]`, `moveCost = [[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]]`
- Output: `17`
- Explanation: Path `5 -> 0 -> 1` contributes cell values $6$ and move costs
  $3+8$.

**Example 2**

- Input: `grid = [[5, 1, 2], [4, 0, 3]]`, `moveCost = [[12, 10, 15], [20, 23, 8], [21, 7, 1], [8, 1, 13], [9, 10, 25], [5, 3, 2]]`
- Output: `6`
- Explanation: Path `2 -> 3` costs $2+1+3=6$.
