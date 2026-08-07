## General
Given two sparse vectors, compute their dot product, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(N + \min(K_1,K_2))$ — Operation count bound.
- **Space Complexity**: $O(K_1+K_2)$ — Auxiliary memory allocation bound.
