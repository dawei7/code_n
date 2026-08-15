# Minimum Operations to Remove Adjacent Ones in Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2123 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Graph Theory, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-remove-adjacent-ones-in-matrix/) |

## Problem Description

### Goal

You are given a zero-indexed binary matrix `grid`. One operation chooses any
cell currently containing `1` and changes it to `0`; zero cells cannot be
changed into ones.

The matrix is well-isolated when no two remaining `1` cells share a horizontal
or vertical edge. Diagonal contact does not count as adjacency. Choose which
ones to remove so that every originally adjacent pair has at least one endpoint
flipped, while using as few operations as possible.

Return that minimum operation count. The positions of the flips themselves are
not required, and disconnected groups of ones are all covered by the same
global minimum.

### Function Contract

**Inputs**

- `grid`: A nonempty $m \times n$ binary matrix.

Let $V=mn$ be the number of grid cells and let $E$ be the number of horizontal
or vertical adjacent pairs whose two cells both contain `1`. Since every cell
has at most four neighbors, $E=O(V)$.

**Return value**

Return the minimum number of `1` cells that must be changed to `0` so that no
two remaining ones are horizontally or vertically adjacent.

### Examples

#### Example 1

- **Input:** `grid = [[1, 1, 0], [0, 1, 1], [1, 1, 1]]`
- **Output:** `3`

Three carefully chosen flips cover every adjacency edge.

#### Example 2

- **Input:** `grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]`
- **Output:** `0`

#### Example 3

- **Input:** `grid = [[0, 1], [1, 0]]`
- **Output:** `0`

The two diagonal ones are already isolated.
