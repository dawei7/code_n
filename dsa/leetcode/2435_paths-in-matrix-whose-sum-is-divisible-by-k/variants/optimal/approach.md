## General
Given a **0-indexed** `m x n` integer matrix `grid` and an integer `k`. You are currently at position `(0, 0)` and you want to reach position $(m - 1, n - 1)$ moving only **down** or **right**, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(mnk)$ — Operation count bound.
- **Space Complexity**: $O(nk)$ — Auxiliary memory allocation bound.
