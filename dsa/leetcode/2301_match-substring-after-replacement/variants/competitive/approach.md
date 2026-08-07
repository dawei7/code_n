## General
Given two strings `s` and `sub`. You are also given a 2D character array `mappings` where $\text{mappings}[i] = [\text{old}_{i}, \text{new}_{i}]$ indicates that you may perform the following operation **any** number of times:, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time.

## Complexity detail
- **Time Complexity**: $O(SP + R)$ — Operation count bound.
- **Space Complexity**: $O(R)$ — Auxiliary memory allocation bound.
