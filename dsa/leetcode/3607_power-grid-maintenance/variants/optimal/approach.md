## General
Given an integer `c` representing `c` power stations, each with a unique identifier `id` from 1 to `c` (1‑based indexing), the algorithm executes a single-pass linear scan through input elements. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O((c + m) \alpha(c) + q + c log c)$ — Operation count bound.
- **Space Complexity**: $O(c + q)$ — Auxiliary memory allocation bound.
