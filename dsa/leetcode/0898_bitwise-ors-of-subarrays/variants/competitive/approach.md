## General
Given an integer array `arr`, return *the number of distinct bitwise ORs of all the non-empty subarrays of* `arr`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(nb)$ — Operation count bound.
- **Space Complexity**: $O(nb)$ — Auxiliary memory allocation bound.
