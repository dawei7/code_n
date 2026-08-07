## General
Given A maze consists of `n` rooms numbered from `1` to `n`, and some rooms are connected by corridors. You are given a 2D integer array `corridors` where $\text{corridors}[i] = [\text{room1}_{i}, \text{room2}_{i}]$ indicat..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n+E^{3/2})$ — Operation count bound.
- **Space Complexity**: $O(n+E)$ — Auxiliary memory allocation bound.
