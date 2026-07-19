# Widest Vertical Area Between Two Points Containing No Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1637 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/) |

## Problem Description
### Goal
You are given $n$ points on a two-dimensional plane, with `points[i] = [xi, yi]`. A vertical area is a fixed-width strip that extends infinitely in both directions along the y-axis.

Find the maximum width of such a strip whose open interior contains no given point. Points lying on either vertical boundary do not count as being inside the area, so they may define the strip's edges.

### Function Contract
**Inputs**

- `points`: an array of $n$ coordinate pairs, where $2 \le n \le 10^5$.
- Each `points[i]` contains exactly two integers `xi` and `yi`, with $0 \le \texttt{xi},\texttt{yi} \le 10^9$.

**Return value**

Return the greatest possible horizontal width of an infinitely tall vertical area containing no point in its open interior.

### Examples
**Example 1**

- Input: `points = [[8,7],[9,9],[7,4],[9,7]]`
- Output: `1`

The occupied x-coordinates are 7, 8, and 9, so either adjacent gap of width 1 is optimal.

**Example 2**

- Input: `points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]`
- Output: `3`

The empty strip bounded by x-coordinates 5 and 8 has width 3.

**Example 3**

- Input: `points = [[0,4],[10,2]]`
- Output: `10`
