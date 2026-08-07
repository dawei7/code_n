## General
Given a **positive** integer `n`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(d^2)$ — Operation count bound.
- **Space Complexity**: $O(d^2)$ — Auxiliary memory allocation bound.
