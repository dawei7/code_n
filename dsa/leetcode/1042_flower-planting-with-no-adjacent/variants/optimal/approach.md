## General
Given You have `n` gardens, labeled from `1` to `n`, and an array `paths` where $\text{paths}[i] = [x_{i}, y_{i}]$ describes a bidirectional path between garden $x_{i}$ to garden $y_{i}$. In each garden, you want to plant o..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(N+P)$ — Operation count bound.
- **Space Complexity**: $O(N+P)$ — Auxiliary memory allocation bound.
