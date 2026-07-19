# Check If It Is a Straight Line

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1232 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-it-is-a-straight-line/) |

## Problem Description

### Goal

You are given an integer array `coordinates`, where each `coordinates[i] = [x, y]` represents a distinct point with integer coordinates in the XY plane.

Check whether every supplied point lies on one straight line; the order in which the points appear has no geometric significance. Return `true` when the entire set is collinear and `false` when at least one point departs from the line determined by the others.

### Function Contract

**Inputs**

- `coordinates`: A list of $n$ distinct points `[x, y]`, where $2\le n\le1000$ and $-10^4\le x,y\le10^4$.

**Return value**

- `true` if all points make a straight line in the XY plane; otherwise, `false`.

### Examples

**Example 1**

- Input: `coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]`
- Output: `true`

Every step increases both coordinates by one, so all points lie on the same diagonal.

**Example 2**

- Input: `coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]`
- Output: `false`

The point `[3,4]` does not lie on the diagonal through `[1,1]` and `[2,2]`.

**Example 3**

- Input: `coordinates = [[0,0],[0,5],[0,-2]]`
- Output: `true`

All three points have the same $x$-coordinate and form a vertical line.
