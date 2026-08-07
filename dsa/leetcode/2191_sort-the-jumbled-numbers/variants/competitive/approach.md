## General
Given a **0-indexed** integer array `mapping` which represents the mapping rule of a shuffled decimal system. $\text{mapping}[i] = j$ means digit `i` should be mapped to digit `j` in this system, the algorithm executes a single-pass linear scan through input elements. Edge case handling: guards against empty/null inputs via early returns, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
