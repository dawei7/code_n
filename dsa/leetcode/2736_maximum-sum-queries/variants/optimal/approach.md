## General
Given two **0-indexed** integer arrays `nums1` and `nums2`, each of length `n`, and a **1-indexed 2D array** `queries` where $\text{queries}[i] = [x_{i}, y_{i}]$, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O((n + q) log(n + q))$ — Operation count bound.
- **Space Complexity**: $O(n + q)$ — Auxiliary memory allocation bound.
