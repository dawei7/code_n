# Painting a Grid With Three Different Colors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1931 |
| Difficulty | Hard |
| Topics | Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/painting-a-grid-with-three-different-colors/) |

## Problem Description
### Goal
An $M \times N$ grid begins with every cell unpainted. Paint every cell with
exactly one of three colors: red, green, or blue. Two cells are adjacent when
they share a horizontal or vertical side, and adjacent cells are not allowed
to receive the same color.

Count all complete colorings that satisfy this adjacency rule. Colorings are
different when at least one cell has a different color. Because the number of
valid grids can be large, return the count modulo $10^9 + 7$.

### Function Contract
**Inputs**

- `m`: the row count $M$, where $1 \le M \le 5$.
- `n`: the column count $N$, where $1 \le N \le 1000$.

For a fixed height $M$, let

$$
S = 3 \cdot 2^{M-1}
$$

be the number of column colorings whose vertically adjacent cells differ.

**Return value**

- The number of valid colorings of the entire grid, reduced modulo
  $10^9 + 7$.

### Examples
**Example 1**

- Input: `m = 1, n = 1`
- Output: `3`

**Example 2**

- Input: `m = 1, n = 2`
- Output: `6`

**Example 3**

- Input: `m = 5, n = 5`
- Output: `580986`
