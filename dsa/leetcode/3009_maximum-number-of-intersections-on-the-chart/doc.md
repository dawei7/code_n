# Maximum Number of Intersections on the Chart

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3009 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Sorting, Sweep Line |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/) |

## Problem Description
### Goal
A line chart contains $N$ points. Point $i$ has horizontal coordinate $i$ and
vertical coordinate `y[i]`, and each consecutive pair is joined by a straight
line segment. Consecutive vertical coordinates are always different, so the
chart has no horizontal segment.

Choose any infinitely long horizontal line. Return the maximum possible number
of distinct intersection points between that line and the chart.

### Function Contract
**Inputs**

- `y`: the vertical coordinates of the chart points in horizontal order

Let $N=\lvert\texttt{y}\rvert$. The contract guarantees
$2\le N\le10^5$, $1\le\texttt{y[i]}\le10^9$, and unequal adjacent
heights.

**Return value**

Return the greatest number of distinct chart intersections achieved by one
horizontal line.

### Examples
**Example 1**

- Input: `y = [1,2,1,2,1,3,2]`
- Output: `5`

A line at height 1.5 crosses five different segments.

**Example 2**

- Input: `y = [2,1,3,4,5]`
- Output: `2`

A line at height 1.5 crosses the first two segments, and no level crosses more.
