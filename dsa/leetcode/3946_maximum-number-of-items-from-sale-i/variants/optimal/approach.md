## General
Given a 2D integer array `items`, where $\text{items}[i] = [\text{factor}_{i}, \text{price}_{i}]$ represents the $$i^{\text{th}}$$ item. You are also given an integer `budget`, the algorithm executes a single-pass linear scan through input elements. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(F log(F) + nB)$ — Operation count bound.
- **Space Complexity**: $O(F + B)$ — Auxiliary memory allocation bound.
