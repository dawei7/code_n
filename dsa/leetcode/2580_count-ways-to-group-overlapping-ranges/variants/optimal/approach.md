## General
Given a 2D integer array `ranges` where $\text{ranges}[i] = [\text{start}_{i}, \text{end}_{i}]$ denotes that all integers between $\text{start}_{i}$ and $\text{end}_{i}$ (both **inclusive**) are contained in the $$i^{\text{..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
