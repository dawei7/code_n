# Maximum Area Rectangle With Point Constraints I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3380 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Binary Indexed Tree, Segment Tree, Geometry, Sorting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/) |

## Problem Description

### Goal

Each entry `[x, y]` in `points` is a unique point on an unbounded plane. Choose four of these points as the corners of a rectangle whose sides are parallel to the coordinate axes. A candidate is valid only when no other supplied point lies strictly inside the rectangle or anywhere on its boundary.

Among all valid rectangles, return the largest area. The four selected corners themselves are permitted on the boundary, but every fifth point within the closed rectangular region invalidates that candidate. Return `-1` if the point set contains no valid rectangle.

### Function Contract

**Inputs**

- `points`: A list of $n$ distinct coordinate pairs `[x, y]`.

The constraints are $1\leq n\leq10$ and $0\leq x,y\leq100$ for every point.

**Return value**

- The maximum area of a valid axis-parallel rectangle, or `-1` when none exists.

### Examples

**Example 1**

- Input: `points = [[1,1],[1,3],[3,1],[3,3]]`
- Output: `4`
- Explanation: The four points form an empty square with width and height two.

**Example 2**

- Input: `points = [[1,1],[1,3],[3,1],[3,3],[2,2]]`
- Output: `-1`
- Explanation: The only possible rectangle contains `[2,2]` in its interior.

**Example 3**

- Input: `points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]`
- Output: `2`
- Explanation: The middle boundary points invalidate the height-two rectangle but serve as corners of valid height-one rectangles.
