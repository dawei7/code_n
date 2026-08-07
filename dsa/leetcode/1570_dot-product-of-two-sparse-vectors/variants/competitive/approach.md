## General
Given two sparse vectors, compute their dot product, the algorithm executes a single-pass linear scan through input elements. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(N + \min(K_1,K_2))$ — Operation count bound.
- **Space Complexity**: $O(K_1+K_2)$ — Auxiliary memory allocation bound.
