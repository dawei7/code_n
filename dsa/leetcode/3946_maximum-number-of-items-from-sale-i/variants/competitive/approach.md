## General
Given a 2D integer array `items`, where $\text{items}[i] = [\text{factor}_{i}, \text{price}_{i}]$ represents the $$i^{\text{th}}$$ item. You are also given an integer `budget`, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(F log(F) + nB)$ — Operation count bound.
- **Space Complexity**: $O(F + B)$ — Auxiliary memory allocation bound.
