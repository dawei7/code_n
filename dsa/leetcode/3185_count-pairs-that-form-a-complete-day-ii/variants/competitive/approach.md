## General
Given an integer array `hours` representing times in **hours**, return an integer denoting the number of pairs `i`, `j` where `i < j` and $\text{hours}[i] + \text{hours}[j]$ forms a **complete day**, the algorithm executes a single-pass linear scan through input elements. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
