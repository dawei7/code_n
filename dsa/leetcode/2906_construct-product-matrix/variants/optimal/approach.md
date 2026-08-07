## General
Given a **0-indexed** 2D integer matrix `grid` of size $n * m$, we define a **0-indexed** 2D matrix `p` of size $n * m$ as the **product** matrix of `grid` if the following condition is met:, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(N)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
