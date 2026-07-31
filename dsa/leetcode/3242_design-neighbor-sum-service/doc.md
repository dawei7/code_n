# Design Neighbor Sum Service

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3242 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Design, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/design-neighbor-sum-service/) |

## Problem Description

### Goal

Create a service for an $n \times n$ matrix `grid`. Its entries are distinct and together contain every integer from $0$ through $n^2-1$.

The constructor `NeighborSum(grid)` stores the matrix. A call to `adjacentSum(value)` must return the sum of the existing orthogonal neighbors of `value`: the cells immediately above, below, left, and right. A call to `diagonalSum(value)` must instead sum the existing four diagonal neighbors: upper-left, upper-right, lower-left, and lower-right. Positions outside the matrix contribute nothing.

Process each requested operation in order. Every queried value occurs in the matrix.

### Function Contract

**Operations**

- `NeighborSum(grid)`: Initializes the service with a square permutation matrix, where $3 \le n \le 10$.
- `adjacentSum(value)`: Returns the sum of the orthogonal neighbors of `value`.
- `diagonalSum(value)`: Returns the sum of the diagonal neighbors of `value`.

At most $2n^2$ query calls follow construction.

**Return value**

For the app-local trace adapter, return one result per operation: `null` for construction and the requested integer sum for each query.

### Examples

**Example 1**

- Input: `operations = ["NeighborSum","adjacentSum","adjacentSum","diagonalSum","diagonalSum"]`, `arguments = [[[[0,1,2],[3,4,5],[6,7,8]]],[1],[4],[4],[8]]`
- Output: `[null,6,16,16,4]`

**Example 2**

- Input: `operations = ["NeighborSum","adjacentSum","diagonalSum"]`, `arguments = [[[[1,2,0,3],[4,7,15,6],[8,9,10,11],[12,13,14,5]]],[15],[9]]`
- Output: `[null,23,45]`

**Example 3**

- Input: `operations = ["NeighborSum","adjacentSum","diagonalSum"]`, `arguments = [[[[8,7,6],[5,4,3],[2,1,0]]],[0],[4]]`
- Output: `[null,4,16]`
