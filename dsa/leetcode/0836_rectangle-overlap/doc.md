# Rectangle Overlap

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 836 |
| Difficulty | Easy |
| Topics | Math, Geometry |
| Official Link | [LeetCode](https://leetcode.com/problems/rectangle-overlap/) |

## Problem Description
### Goal
An axis-aligned rectangle is represented as `[x1, y1, x2, y2]`. The point `(x1, y1)` is its bottom-left corner and `(x2, y2)` is its top-right corner; its horizontal edges are parallel to the x-axis and its vertical edges are parallel to the y-axis.

Two rectangles overlap only when their intersection has positive area. Rectangles that merely share an edge or a corner do not overlap. Given valid nonzero-area rectangles `rec1` and `rec2`, return `true` if they overlap and `false` otherwise.

### Function Contract
**Inputs**

- `rec1`: four integers `[x1, y1, x2, y2]` describing the first axis-aligned rectangle.
- `rec2`: four integers in the same bottom-left/top-right format.
- Every coordinate lies in $[-10^9,10^9]$, and each rectangle has positive width and height.

**Return value**

Return a boolean indicating whether the intersection of the two rectangles has positive area.

### Examples
**Example 1**

- Input: `rec1 = [0, 0, 2, 2], rec2 = [1, 1, 3, 3]`
- Output: `true`

**Example 2**

- Input: `rec1 = [0, 0, 1, 1], rec2 = [1, 0, 2, 1]`
- Output: `false`

The rectangles share an edge but have no positive-area intersection.

**Example 3**

- Input: `rec1 = [0, 0, 1, 1], rec2 = [2, 2, 3, 3]`
- Output: `false`
