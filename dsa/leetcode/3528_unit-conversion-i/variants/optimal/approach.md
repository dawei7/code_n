## General
Given There are `n` types of units indexed from `0` to $n - 1$. You are given a 2D integer array `conversions` of length $n - 1$, where $\text{conversions}[i] = [\text{sourceUnit}_{i}, \text{targetUnit}_{i}, \text{conversio..., the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
