# Find Nearest Point That Has the Same X or Y Coordinate

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1779 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/) |

## Problem Description

### Goal

Your current location on a Cartesian grid is `(x, y)`. Each entry `points[i] = [a_i, b_i]` gives the coordinates of another point. A point is valid when it shares either the same x-coordinate or the same y-coordinate with your location.

Among the valid points, find one with the smallest Manhattan distance from `(x, y)`. Return its zero-based index. If several valid points have the same minimum distance, return the smallest of their indices; if no point is valid, return `-1`. A point exactly at the current location is valid and has distance zero.

### Function Contract

**Inputs**

- `x`, `y`: the current coordinates.
- `points`: an array of $n$ coordinate pairs.
- The constraints guarantee $1 \le n \le 10^4$ and all coordinates lie between $1$ and $10^4$.

**Return value**

Return the smallest index minimizing

$$
\lvert a_i-x\rvert+\lvert b_i-y\rvert
$$

among indices satisfying $a_i=x$ or $b_i=y$. Return `-1` if that set is empty.

### Examples

**Example 1**

- Input: `x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]`
- Output: `2`
- Explanation: Indices `2` and `4` are both one unit away, so the smaller index is returned.

**Example 2**

- Input: `x = 3, y = 4, points = [[3,4]]`
- Output: `0`
- Explanation: The point equals the current location and has distance zero.

**Example 3**

- Input: `x = 3, y = 4, points = [[2,3]]`
- Output: `-1`
- Explanation: The point shares neither coordinate.
