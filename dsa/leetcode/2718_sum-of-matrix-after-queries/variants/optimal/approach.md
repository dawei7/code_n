## General
Given an integer `n` and a **0-indexed** **2D array** `queries` where $\text{queries}[i] = [\text{type}_{i}, \text{index}_{i}, \text{val}_{i}]$, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time.

## Complexity detail
- **Time Complexity**: $O(q)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
