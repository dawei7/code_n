# Minimum Area Rectangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 939 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Geometry, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-area-rectangle/) |

## Problem Description

### Goal

Given distinct points `points` in the X-Y plane, find the minimum area of a rectangle whose four vertices all occur in the input and whose sides are parallel to the X and Y axes.

An axis-aligned rectangle requires two different x-coordinates and two different y-coordinates, with all four coordinate combinations present. Return its smallest positive area. If the supplied points cannot form any such rectangle, return `0`.

### Function Contract

**Inputs**

- `points`: a list of $N$ distinct pairs `[x, y]`, where $1 \le N \le 500$ and $0 \le x,y \le 4 \cdot 10^4$.

**Return value**

Return the minimum area of an axis-aligned rectangle using four input points, or `0` if none exists.

### Examples

**Example 1**

- Input: `points = [[1,1],[1,3],[3,1],[3,3],[2,2]]`
- Output: `4`

**Example 2**

- Input: `points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]`
- Output: `2`
