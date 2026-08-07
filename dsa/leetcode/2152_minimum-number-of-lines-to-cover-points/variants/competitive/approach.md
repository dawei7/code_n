## General
Given an array `points` where $\text{points}[i] = [x_{i}, y_{i}]$ represents a point on an **X-Y **plane, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n^3 + n * 2^n)$ — Operation count bound.
- **Space Complexity**: $O(n^2 + 2^n)$ — Auxiliary memory allocation bound.
