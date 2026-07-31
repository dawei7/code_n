# Count Lattice Points Inside a Circle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2249 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Geometry, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/count-lattice-points-inside-a-circle/) |

## Problem Description

### Goal

Each entry `[x, y, r]` in `circles` describes a circle centered at integer
coordinates $(x,y)$ with radius $r$. A lattice point has two integer
coordinates. It belongs to a circle when it lies in the circle's interior or
on its circumference.

Count how many distinct lattice points belong to at least one supplied circle.
A point covered by several overlapping circles contributes only once.

### Function Contract

**Inputs**

- `circles`: Between $1$ and $200$ triples `[x, y, r]`, where $1\le x,y\le100$ and $1\le r\le\min(x,y)$.

**Return value**

Return the number of distinct integer-coordinate points whose Euclidean
distance from at least one circle center is no greater than that circle's
radius.

### Examples

**Example 1**

- Input: `circles = [[2,2,1]]`
- Output: `5`

**Example 2**

- Input: `circles = [[2,2,2],[3,4,1]]`
- Output: `16`

**Example 3**

- Input: `circles = [[1,1,1],[1,1,1]]`
- Output: `5`
