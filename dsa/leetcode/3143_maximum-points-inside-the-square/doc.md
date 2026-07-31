# Maximum Points Inside the Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3143 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-points-inside-the-square/) |

## Problem Description
### Goal
You are given distinct points in the plane through the array `points`, together with a string `s`. The character `s[i]` is the tag assigned to `points[i]`.

Consider squares centered at the origin whose edges are parallel to the coordinate axes. Such a square is valid when it does not contain two points with the same tag. Points on the boundary count as contained, and a square may have side length zero. Return the greatest number of points that can be contained by a valid square.

### Function Contract
**Inputs**

- `points`: A list of distinct coordinate pairs `[x, y]`.
- `s`: A lowercase string of equal length whose character at each index tags the corresponding point.

Let $n = \lvert\texttt{points}\rvert = \lvert\texttt{s}\rvert$. The constraints are $1 \le n \le 10^5$ and $-10^9 \le \texttt{points[i][0]}, \texttt{points[i][1]} \le 10^9$.

**Return value**

Return the maximum number of points inside or on the boundary of an axis-aligned square centered at the origin that contains no repeated tag.

### Examples
**Example 1**

- Input: `points = [[2, 2], [-1, -2], [-4, 4], [-3, 1], [3, -3]], s = "abdca"`
- Output: `2`
- Explanation: A square of side length $4$ contains the first two points, whose tags differ. Enlarging it enough to gain more points eventually introduces a repeated tag.

**Example 2**

- Input: `points = [[1, 1], [-2, -2], [-2, 2]], s = "abb"`
- Output: `1`
- Explanation: The nearest point can be included alone, but reaching the two farther points would include both occurrences of tag `b`.

**Example 3**

- Input: `points = [[1, 1], [-1, -1], [2, -2]], s = "ccd"`
- Output: `0`
- Explanation: The two nearest points have the same tag and enter at the same boundary, so no valid square can contain either one.
