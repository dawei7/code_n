# Maximum Difference Score in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3148 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-difference-score-in-a-grid/) |

## Problem Description

### Goal

You are given an $m \times n$ matrix `grid` containing positive integers. From a cell, one move may go to any other cell strictly below it in the same column or strictly to its right in the same row. The destination does not need to be adjacent. Moving from a cell whose value is `c1` to one whose value is `c2` contributes `c2 - c1` to the score.

Choose any starting cell and make one or more valid moves. A route may combine rightward and downward moves, but it can never move left or upward. Return the greatest total score achievable. At least one move is mandatory, so remaining at a single high-valued cell is not a valid route.

### Function Contract

**Inputs**

- `grid`: An $m \times n$ matrix of positive integers, where $2 \le m,n \le 1000$, $4 \le mn \le 10^5$, and $1 \le \texttt{grid[i][j]} \le 10^5$.

**Return value**

Return the maximum total score over every route containing at least one valid move. The result may be negative.

### Examples

#### Example 1

- **Input:** `grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]`
- **Output:** `9`
- **Explanation:** Move from value `5` at `(0, 1)` down to `7`, then right to `14`. The scores `2` and `7` total `9`.

#### Example 2

- **Input:** `grid = [[4,3,2],[3,2,1]]`
- **Output:** `-1`
- **Explanation:** Every valid destination is smaller than its start; one move from `4` to an adjacent `3` loses only one point, which is optimal.

#### Example 3

- **Input:** `grid = [[1,2,3],[4,5,6],[7,8,50]]`
- **Output:** `49`
- **Explanation:** A rightward move followed by a downward move can connect the upper-left `1` to the lower-right `50`, and the intermediate scores telescope to `50 - 1`.
