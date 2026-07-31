# Minimum Rectangles to Cover Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3111 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [minimum-rectangles-to-cover-points](https://leetcode.com/problems/minimum-rectangles-to-cover-points/) |

## Problem Description

### Goal

You are given a set of distinct points `points` in the nonnegative part of the coordinate plane and a nonnegative integer `w`. Cover every point using axis-aligned rectangles whose lower side lies on the $x$-axis. A rectangle may begin at $(x_1,0)$ and end at $(x_2,y_2)$ for any $x_1 \le x_2$ and $y_2 \ge 0$, provided its horizontal width satisfies $x_2-x_1 \le w$.

A point on a rectangle's interior or boundary is covered, and rectangles may overlap or cover the same point more than once. Their heights are unrestricted, so each can be made tall enough for every point in its horizontal span. Return the minimum number of rectangles needed to cover all given points.

### Function Contract

**Inputs**

- `points`: A list of $n$ distinct coordinate pairs `[x, y]`, where $1 \le n \le 10^5$ and $0 \le x,y \le 10^9$.
- `w`: The maximum horizontal width of each rectangle, where $0 \le w \le 10^9$.

**Return value**

- The minimum number of valid rectangles whose union covers every point.

### Examples

**Example 1**

- Input: `points = [[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]], w = 1`
- Output: `2`
- Explanation: Horizontal spans $[1,2]$ and $[3,4]$ cover every point.

**Example 2**

- Input: `points = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]], w = 2`
- Output: `3`
- Explanation: Spans $[0,2]$, $[3,5]$, and $[6,6]$ are sufficient.

**Example 3**

- Input: `points = [[2,3],[1,2]], w = 0`
- Output: `2`
- Explanation: A zero-width rectangle covers only one distinct $x$-coordinate.
