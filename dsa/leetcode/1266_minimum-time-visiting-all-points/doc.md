# Minimum Time Visiting All Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1266 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-visiting-all-points/) |

## Problem Description

### Goal

An array gives $n$ points with integer coordinates on a 2D plane. Starting at the first point, visit every point in exactly the order in which it appears. Passing through a point scheduled for later does not visit it early; it counts only when its position in the required sequence is reached.

During one second, you may move one unit horizontally, one unit vertically, or one unit in each direction simultaneously. The last option is a diagonal move of Euclidean length $\sqrt{2}$. Return the minimum total number of seconds needed to complete the ordered visit.

### Function Contract

**Inputs**

- `points`: an ordered array of $n$ coordinate pairs `points[i] = [x_i, y_i]`, where $1 \le n \le 100$ and $-1000 \le x_i,y_i \le 1000$.

**Return value**

- Return the minimum time in seconds required to visit all points in their given order.

### Examples

**Example 1**

- Input: `points = [[1,1],[3,4],[-1,0]]`
- Output: `7`

**Example 2**

- Input: `points = [[3,2],[-2,2]]`
- Output: `5`

**Example 3**

- Input: `points = [[0,0],[0,0],[2,1]]`
- Output: `2`
