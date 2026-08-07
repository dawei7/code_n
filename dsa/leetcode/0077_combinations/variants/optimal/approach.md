## General
Given two integers `n` and `k`, return *all possible combinations of* `k` *numbers chosen from the range* `[1, n]`, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(k \cdot C(n,k))$ — Operation count bound.
- **Space Complexity**: $O(k)$ — Auxiliary memory allocation bound.
