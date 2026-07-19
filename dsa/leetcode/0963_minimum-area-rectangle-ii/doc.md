# Minimum Area Rectangle II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 963 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [minimum-area-rectangle-ii](https://leetcode.com/problems/minimum-area-rectangle-ii/) |

## Problem Description

### Goal

You are given distinct points in the Cartesian plane, with each point represented as `[x, y]`. Select four of them that are the vertices of a rectangle. The rectangle may be rotated by any angle; its sides are not required to be parallel to the coordinate axes.

Among every rectangle that can be formed entirely from the supplied points, return the smallest area. If no four points form a rectangle, return `0`. A floating-point answer is accepted when it differs from the exact area by at most $10^{-5}$.

### Function Contract

**Inputs**

- `points`: a list of $P$ distinct coordinate pairs, where $1 \le P \le 50$.
- Each coordinate is an integer between $0$ and $4\times10^4$, inclusive.

**Return value**

Return the minimum area of a rectangle whose four vertices belong to `points`, or `0` if none exists.

### Examples

**Example 1**

- Input: `points = [[1,2],[2,1],[1,0],[0,1]]`
- Output: `2.00000`

**Example 2**

- Input: `points = [[0,1],[2,1],[1,1],[1,0],[2,0]]`
- Output: `1.00000`

**Example 3**

- Input: `points = [[0,3],[1,2],[3,1],[1,3],[2,1]]`
- Output: `0`
