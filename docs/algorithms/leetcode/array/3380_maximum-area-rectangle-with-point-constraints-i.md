# Maximum Area Rectangle With Point Constraints I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3380 |
| Difficulty | Medium |
| Topics | Array, Math, Geometry, Sorting, Enumeration |
| Official Link | [maximum-area-rectangle-with-point-constraints-i](https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/) |

## Problem Description & Examples
### Goal
Given a set of 2D points, identify the largest possible area of a rectangle whose sides are parallel to the coordinate axes, such that all four vertices of the rectangle are present in the input set, and no other points from the input set lie strictly inside or on the boundary of the rectangle.

### Function Contract
**Inputs**

- `points`: A list of lists, where each inner list `[x, y]` represents the coordinates of a point in a 2D plane.

**Return value**

- An integer representing the maximum area found. If no such rectangle exists, return -1.

### Examples
**Example 1**

- Input: `points = [[1,1],[1,3],[3,1],[3,3],[2,2]]`
- Output: `-1`
- Explanation: The rectangle formed by (1,1), (1,3), (3,1), (3,3) contains the point (2,2), so it is invalid.

**Example 2**

- Input: `points = [[1,1],[1,3],[3,1],[3,3]]`
- Output: `4`
- Explanation: The rectangle formed by these four points has area (3-1) * (3-1) = 4.

**Example 3**

- Input: `points = [[0,0],[1,1],[0,1],[1,0]]`
- Output: `1`

---

## Underlying Base Algorithm(s)
The algorithm uses a hash set for $O(1)$ point lookups. We iterate through all pairs of points that could serve as diagonal vertices of a rectangle. For each pair $(x1, y1)$ and $(x2, y2)$, we check if the other two required vertices $(x1, y2)$ and $(x2, y1)$ exist in the set. If they do, we verify the "empty" constraint by iterating through all input points to ensure no other point falls within the rectangle's bounds.

---

## Complexity Analysis
- **Time Complexity**: $O(N^3)$, where $N$ is the number of points. We iterate over $O(N^2)$ pairs of points, and for each valid rectangle, we perform an $O(N)$ check to ensure no points are inside.
- **Space Complexity**: $O(N)$ to store the points in a hash set for efficient lookup.
