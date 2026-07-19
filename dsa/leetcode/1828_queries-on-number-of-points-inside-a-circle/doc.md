# Queries on Number of Points Inside a Circle

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/) |
| Frontend ID | 1828 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given a list of points on the two-dimensional plane. Each point is represented as `[x, y]`, and several points may occupy the same coordinates; every occurrence is still a separate point.

Each query is `[xCenter, yCenter, radius]` and describes a circle. For every query, count the input points that lie inside the circle or exactly on its circumference. Return the counts in the same order as the queries.

### Function Contract

**Inputs**

- `points`: a list of $p$ integer coordinate pairs `[x, y]`, where $1 \le p \le 500$ and $0 \le x, y \le 500$.
- `queries`: a list of $q$ triples `[xCenter, yCenter, radius]`, where $1 \le q \le 500$, $0 \le \texttt{xCenter}, \texttt{yCenter} \le 500$, and $1 \le \texttt{radius} \le 500$.

**Return value**

- Return a list of $q$ integers. Entry $j$ is the number of occurrences in `points` whose coordinates are inside or on the circle described by `queries[j]`.

### Examples

**Example 1**

- Input: `points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]`
- Output: `[3,2,2]`

For the first query, `[1,3]` and `[3,3]` are on the boundary, while `[2,2]` is inside.

**Example 2**

- Input: `points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]`
- Output: `[2,3,2,4]`

**Example 3**

- Input: `points = [[0,0],[0,0],[3,4],[6,0]], queries = [[0,0,5]]`
- Output: `[3]`

Both copies of `[0,0]` count, and `[3,4]` lies exactly on the circumference.
