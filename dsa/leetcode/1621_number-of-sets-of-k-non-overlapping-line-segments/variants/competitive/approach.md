## General
Given `n` points on a 1-D plane, where the $$i^{\text{th}}$$ point (from `0` to `n-1`) is at $x = i$, find the number of ways we can draw **exactly** `k` **non-overlapping** line segments such that each segment covers two o..., the algorithm executes a single-pass linear scan through input elements. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(k+\log M)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
