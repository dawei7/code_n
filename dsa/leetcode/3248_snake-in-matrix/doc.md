# Snake in Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3248 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/snake-in-matrix/) |

## Problem Description

### Goal

An $n \times n$ matrix numbers its cells in row-major order: the cell at row $i$ and column $j$ has position $in+j$. A snake begins at position `0`, the upper-left cell.

Execute every string in `commands` in order. `UP` and `DOWN` move one row, while `LEFT` and `RIGHT` move one column. The input guarantees that every intermediate move remains inside the matrix.

Return the row-major position of the cell occupied after the final command.

### Function Contract

**Inputs**

- `n`: The side length of the square matrix, where $2 \le n \le 10$.
- `commands`: Between 1 and 100 strings, each equal to `UP`, `RIGHT`, `DOWN`, or `LEFT`; the complete path is in bounds.

**Return value**

- The final flattened cell position $in+j$.

### Examples

#### Example 1

- **Input:** `n = 2, commands = ["RIGHT","DOWN"]`
- **Output:** `3`

#### Example 2

- **Input:** `n = 3, commands = ["DOWN","RIGHT","UP"]`
- **Output:** `1`

#### Example 3

- **Input:** `n = 4, commands = ["DOWN","DOWN","RIGHT","UP"]`
- **Output:** `5`
