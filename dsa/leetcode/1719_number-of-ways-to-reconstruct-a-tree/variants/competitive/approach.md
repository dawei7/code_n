## General
Given an array `pairs`, where $\text{pairs}[i] = [x_{i}, y_{i}]$, and:, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(V^2)$ — Operation count bound.
- **Space Complexity**: $O(V^2)$ — Auxiliary memory allocation bound.
