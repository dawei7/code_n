## General
Given a **0-indexed** integer array `nums`, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends, a dynamic programming memoization table to cache intermediate subproblem states.

## Complexity detail
- **Time Complexity**: $O(N)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
