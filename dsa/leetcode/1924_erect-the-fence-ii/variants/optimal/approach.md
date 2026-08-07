## General
Given a 2D integer array `trees` where $\text{trees}[i] = [x_{i}, y_{i}]$ represents the location of the $$i^{\text{th}}$$ tree in the garden, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(N)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
