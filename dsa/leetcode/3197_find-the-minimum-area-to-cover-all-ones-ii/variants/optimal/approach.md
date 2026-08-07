## General
Given a 2D **binary** array `grid`. You need to find 3 **non-overlapping** rectangles having **non-zero** areas with horizontal and vertical sides such that all the 1's in `grid` lie inside these rectangles, the algorithm executes a single-pass linear scan through input elements.

## Complexity detail
- **Time Complexity**: $O((R + C)(R^2 + RC + C^2))$ — Operation count bound.
- **Space Complexity**: $O(RC + R^2 + C^2)$ — Auxiliary memory allocation bound.
