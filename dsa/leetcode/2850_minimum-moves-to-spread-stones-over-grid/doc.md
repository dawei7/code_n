# Minimum Moves to Spread Stones Over Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2850 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Matrix, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/) |

## Problem Description

### Goal

You receive a 0-indexed $3 \times 3$ integer matrix `grid`. Each entry gives the number of stones currently occupying that cell. There are exactly nine stones across the entire grid, although one cell may initially hold several of them and another may be empty.

One move transfers a single stone between two cells that share a side. Diagonal cells are not adjacent, so moving a stone between them requires more than one move through side-sharing cells.

Return the minimum number of moves needed to finish with exactly one stone in every cell.

### Function Contract

**Inputs**

- `grid`: A $3 \times 3$ matrix whose entries are integers from $0$ through $9$ and whose total is exactly $9$.

Let $k$ be the number of empty cells. Because the grid contains nine cells and nine stones, $k$ is also the number of surplus stones that must be moved, and $0 \le k \le 8$.

**Return value**

- The minimum number of side-adjacent single-stone moves required to place one stone in each cell.

### Examples

#### Example 1

- **Input:** `grid = [[1,1,0],[1,1,1],[1,2,1]]`
- **Output:** `3`
- **Explanation:** The extra stone at `(2,1)` can travel right once and then upward twice until it reaches `(0,2)`. Those three side-adjacent transfers fill the only empty cell, and no shorter route exists.

#### Example 2

- **Input:** `grid = [[1,3,0],[1,0,0],[1,0,3]]`
- **Output:** `4`
- **Explanation:** Two extra stones from `(0,1)` fill `(0,2)` and `(1,1)`, while two extras from `(2,2)` fill `(1,2)` and `(2,1)`. Each transfer travels one edge, for four moves in total.
