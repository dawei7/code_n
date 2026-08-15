# Count Unguarded Cells in the Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2257 |
| Difficulty | Medium |
| Topics | Array, Matrix, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/count-unguarded-cells-in-the-grid/) |

## Problem Description

### Goal

An $m\times n$ 0-indexed grid contains guards, walls, and unoccupied cells.
The arrays `guards` and `walls` give the distinct coordinates of every
occupied position.

Each guard sees horizontally and vertically in the four cardinal directions.
Its view continues through unoccupied cells until either a wall or another
guard blocks that direction. An unoccupied cell is guarded when at least one
guard can see it; being visible from several directions does not change its
status.

Count and return the unoccupied cells that no guard can see. Guard and wall
positions themselves are occupied and must never be included in the count.

### Function Contract

**Inputs**

- `m`: The number of rows, between $1$ and $10^5$.
- `n`: The number of columns, between $1$ and $10^5$, with $2\le mn\le10^5$.
- `guards`: Between $1$ and $5\cdot10^4$ unique coordinates `[row, column]`.
- `walls`: Between $1$ and $5\cdot10^4$ unique coordinates `[row, column]`.

All guard and wall positions are mutually distinct, lie inside the grid, and
their combined count is at most $mn$.

**Return value**

Return the number of coordinates that contain neither a guard nor a wall and
have no unobstructed guard in the same row or column.

### Examples

#### Example 1

- **Input:** `m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]`
- **Output:** `7`

#### Example 2

- **Input:** `m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]`
- **Output:** `4`

#### Example 3

- **Input:** `m = 2, n = 2, guards = [[0,0]], walls = [[1,1]]`
- **Output:** `0`
