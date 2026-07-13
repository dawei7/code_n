# Minimum Path Cost in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2304 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-path-cost-in-a-grid](https://leetcode.com/problems/minimum-path-cost-in-a-grid/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-path-cost-in-a-grid/).

### Goal
Choose one cell from every grid row, moving from a cell in row `r` to any column in row `r + 1`. Path cost is the sum of visited cell values plus a transition cost determined by the current cell's value and the destination column. Minimize total cost.

### Function Contract
**Inputs**

- `grid`: a matrix of distinct nonnegative values.
- `moveCost`: `moveCost[value][next_column]` gives the transition cost.

**Return value**

The minimum cost of a top-to-bottom path.

### Examples
**Example 1**

- Input: `grid = [[5, 3], [4, 0], [2, 1]]`, `moveCost = [[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]]`
- Output: `17`

**Example 2**

- Input: `grid = [[1, 0]]`, `moveCost = [[0, 0], [0, 0]]`
- Output: `0`

**Example 3**

- Input: `grid = [[0], [1]]`, `moveCost = [[2], [0]]`
- Output: `3`

---

## Solution
### Approach
Use row-by-row dynamic programming. Let the current cost at column `c` include all visited values through that cell. For every next-row column `d`, relax with `current[c] + moveCost[grid[r][c]][d] + grid[r + 1][d]`. The minimum value after the final row is the answer.

### Complexity Analysis
- **Time Complexity**: `O(mn^2)`
- **Space Complexity**: `O(n)` with rolling rows

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
