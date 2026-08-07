## General
Given a string `s` of lowercase English letters and a 2D integer array `shifts` where $\text{shifts}[i] = [\text{start}_{i}, \text{end}_{i}, \text{direction}_{i}]$. For every `i`, **shift** the characters in `s` from the in..., the algorithm executes a single-pass linear scan through input elements. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n+m)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
