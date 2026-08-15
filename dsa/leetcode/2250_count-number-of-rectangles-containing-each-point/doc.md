# Count Number of Rectangles Containing Each Point

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2250 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Binary Indexed Tree, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/) |

## Problem Description

### Goal

Each entry `[length, height]` in `rectangles` describes an axis-aligned
rectangle whose bottom-left corner is $(0,0)$ and whose top-right corner is
`(length, height)`. Each entry `[x, y]` in `points` is a query point.

For every query, count the rectangles that contain it. Rectangle boundaries
are included, so containment requires both $x\le\texttt{length}$ and
$y\le\texttt{height}$. Return the counts in the same order as the query
points.

### Function Contract

**Inputs**

- `rectangles`: Between $1$ and $5\cdot10^4$ distinct pairs `[length, height]`, where $1\le\texttt{length}\le10^9$ and $1\le\texttt{height}\le100$.
- `points`: Between $1$ and $5\cdot10^4$ distinct pairs `[x, y]`, where $1\le x\le10^9$ and $1\le y\le100$.

**Return value**

Return one integer per point, preserving input order, equal to the number of
rectangles whose width and height both reach that point.

### Examples

#### Example 1

- **Input:** `rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]`
- **Output:** `[2,1]`

#### Example 2

- **Input:** `rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[1,1]]`
- **Output:** `[1,3]`

#### Example 3

- **Input:** `rectangles = [[4,2]], points = [[5,1],[4,2]]`
- **Output:** `[0,1]`
