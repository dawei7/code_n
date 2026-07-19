# Minimum Cost Homecoming of a Robot in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2087 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/) |

## Problem Description

### Goal

An $m \times n$ grid has its top-left cell at `(0, 0)`. A robot starts at `startPos = [startRow, startCol]` and must reach `homePos = [homeRow, homeCol]`. On each move it may enter one orthogonally adjacent cell without leaving the grid.

Moving vertically into row $r$ costs `rowCosts[r]`, while moving horizontally into column $c$ costs `colCosts[c]`. Costs may be zero, and the starting cell itself incurs no entry cost. Return the minimum total cost of a route from the start to home.

### Function Contract

**Inputs**

- `startPos`: the valid starting coordinates `[startRow, startCol]`.
- `homePos`: the valid destination coordinates `[homeRow, homeCol]`.
- `rowCosts`: $m$ nonnegative row-entry costs.
- `colCosts`: $n$ nonnegative column-entry costs.
- $1 \le m,n \le 10^5$, and every entry cost is between $0$ and $10^4$.

Let the required Manhattan travel distance be

$$
D = \lvert \textit{homeRow} - \textit{startRow} \rvert
  + \lvert \textit{homeCol} - \textit{startCol} \rvert.
$$

**Return value**

Return the minimum total cost needed to reach `homePos`.

### Examples

**Example 1**

- Input: `startPos = [1, 0]`, `homePos = [2, 3]`, `rowCosts = [5, 4, 3]`, `colCosts = [8, 2, 6, 7]`
- Output: `18`
- Explanation: Enter row `2` for cost `3`, then columns `1`, `2`, and `3` for costs `2`, `6`, and `7`.

**Example 2**

- Input: `startPos = [0, 0]`, `homePos = [0, 0]`, `rowCosts = [5]`, `colCosts = [26]`
- Output: `0`
- Explanation: The robot is already home, so it makes no moves.
