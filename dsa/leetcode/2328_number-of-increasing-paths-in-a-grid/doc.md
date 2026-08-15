# Number of Increasing Paths in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2328 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort, Memoization, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/) |

## Problem Description

### Goal

Given an $m$ by $n$ integer matrix `grid`, form a path by starting at any cell
and repeatedly moving to an orthogonally adjacent cell: up, down, left, or
right. Every move must go to a strictly larger value, while a path containing
only its starting cell is also valid.

Count all such strictly increasing paths, allowing a path to end at any cell.
Two paths are different whenever their sequences of visited cell positions are
not exactly the same, even if the corresponding value sequences match. Return
the total modulo $10^9+7$.

### Function Contract

**Inputs**

- `grid`: A nonempty rectangular integer matrix with $m$ rows and $n$ columns,
  where $1 \le m,n \le 1000$, $1 \le mn \le 10^5$, and every entry lies in
  $[1,10^5]$.

**Return value**

The number of position-distinct strictly increasing four-directional paths in
`grid`, modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `grid = [[1,1],[3,4]]`
- **Output:** `8`
- **Explanation:** Four one-cell paths, three two-cell paths, and the path from
  the lower-left `1` through `3` to `4` give eight paths altogether.

#### Example 2

- **Input:** `grid = [[1],[2]]`
- **Output:** `3`
- **Explanation:** The two single-cell paths and the path from `1` to `2` are
  valid.

#### Example 3

- **Input:** `grid = [[5,5,5],[5,5,5]]`
- **Output:** `6`
- **Explanation:** Equal values cannot follow one another in a strictly
  increasing path, so only the six individual cells count.
