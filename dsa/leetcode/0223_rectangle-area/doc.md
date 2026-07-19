# Rectangle Area

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 223 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/rectangle-area/) |

## Problem Description
### Goal
Two axis-aligned rectangles are described by their lower-left and upper-right corner coordinates. Each rectangle has positive width and height, and the rectangles may be separate, touch along a boundary, overlap partially, or place one entirely inside the other.

Return the total plane area covered by at least one rectangle. Areas covered by both rectangles must be counted only once, while touching edges or corners contribute zero overlap. Coordinates may be negative, but width and height come from coordinate differences. The function returns only the union area, not the intersection rectangle or a set of boundary points.

### Function Contract
**Inputs**

- `ax1, ay1, ax2, ay2`: lower-left and upper-right corners of rectangle A
- `bx1, by1, bx2, by2`: corresponding corners of rectangle B

**Return value**

The total plane area covered by at least one rectangle.

### Examples
**Example 1**

- Input: `A=(-3,0)-(3,4), B=(0,-1)-(9,2)`
- Output: `45`

**Example 2**

- Identical two-by-two rectangles
- Output: `4`

**Example 3**

- Disjoint rectangles
- Output: the sum of their areas
