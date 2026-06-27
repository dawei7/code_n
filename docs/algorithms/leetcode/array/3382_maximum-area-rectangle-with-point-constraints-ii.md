# Maximum Area Rectangle With Point Constraints II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3382 |
| Difficulty | Hard |
| Topics | Array, Math, Binary Indexed Tree, Segment Tree, Geometry, Sorting |
| Official Link | [maximum-area-rectangle-with-point-constraints-ii](https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/) |

## Problem Description & Examples
### Goal
Given a set of points in a 2D plane, find the maximum area of a rectangle whose sides are parallel to the coordinate axes, such that all four corners of the rectangle are present in the input set, and no other points from the input set lie strictly inside or on the boundary of the rectangle.

### Function Contract
**Inputs**

- `x`: A list of integers representing the x-coordinates of the points.
- `y`: A list of integers representing the y-coordinates of the points.

**Return value**

- An integer representing the maximum area found, or -1 if no such rectangle exists.

### Examples
**Example 1**

- Input: `x = [1, 1, 3, 3], y = [1, 3, 1, 3]`
- Output: `4`

**Example 2**

- Input: `x = [1, 1, 3, 3, 2, 2], y = [1, 3, 1, 3, 2, 2]`
- Output: `-1`

**Example 3**

- Input: `x = [1, 1, 2, 2, 3, 3], y = [1, 2, 1, 2, 1, 2]`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem is solved by grouping points by their x-coordinates and identifying potential vertical segments. By sorting these segments by their x-coordinates, we can use a sweep-line approach combined with a Fenwick Tree (Binary Indexed Tree) or a Segment Tree to efficiently query the existence of points within a specific y-range. The constraint of "no points inside" is handled by verifying that no points exist between the two vertical edges of a candidate rectangle.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)`, where N is the number of points. This accounts for sorting the points and performing sweep-line operations with logarithmic time queries.
- **Space Complexity**: `O(N)` to store the points, the coordinate mapping, and the auxiliary data structures used for the sweep-line.
