## General
Given a **0-indexed** integer array `nums` representing the contents of a **pile**, where $\text{nums}[0]$ is the topmost element of the pile, the algorithm executes a single-pass linear scan through input elements. Edge case handling: guards against empty/null inputs via early returns, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(min(n, k))$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
