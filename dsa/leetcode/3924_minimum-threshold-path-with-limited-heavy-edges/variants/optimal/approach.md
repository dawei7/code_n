## General
Given There is an undirected weighted graph with `n` nodes labeled from 0 to $n - 1$, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n log m + m log m)$ — Operation count bound.
- **Space Complexity**: $O(n + m)$ — Auxiliary memory allocation bound.
