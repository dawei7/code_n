## General
Given There is a 1 million by 1 million grid on an XY-plane, and the coordinates of each grid square are `(x, y)`, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(B^2)$ — Operation count bound.
- **Space Complexity**: $O(B^2)$ — Auxiliary memory allocation bound.
