## General
Given two integers `n` and `m` which represent the size of a **1-indexed **grid. You are also given an integer `k`, a **1-indexed** integer array `source` and a **1-indexed** integer array `dest`, where `source` and `dest` ..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(k)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
