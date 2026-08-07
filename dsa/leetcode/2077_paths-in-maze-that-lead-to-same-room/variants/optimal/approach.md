## General
Given A maze consists of `n` rooms numbered from `1` to `n`, and some rooms are connected by corridors. You are given a 2D integer array `corridors` where $\text{corridors}[i] = [\text{room1}_{i}, \text{room2}_{i}]$ indicat..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n+E^{3/2})$ — Operation count bound.
- **Space Complexity**: $O(n+E)$ — Auxiliary memory allocation bound.
