## General
Given an unrooted weighted tree with `n` vertices representing servers numbered from `0` to $n - 1$, an array `edges` where $\text{edges}[i] = [a_{i}, b_{i}, \text{weight}_{i}]$ represents a bidirectional edge between verti..., the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n^2)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
