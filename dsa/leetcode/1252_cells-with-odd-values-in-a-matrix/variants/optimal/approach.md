## General
Given There is an `m x n` matrix that is initialized to all `0`'s. There is also a 2D array `indices` where each $\text{indices}[i] = [r_{i}, c_{i}]$ represents a **0-indexed location** to perform some increment operations ..., the algorithm executes a single-pass linear scan through input elements. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(m+n+k)$ — Operation count bound.
- **Space Complexity**: $O(m+n)$ — Auxiliary memory allocation bound.
