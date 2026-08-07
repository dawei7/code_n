## General
Given There is a safe protected by a password. The password is a sequence of `n` digits where each digit can be in the range `[0, k - 1]`, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(k^n)$ — Operation count bound.
- **Space Complexity**: $O(k^n)$ — Auxiliary memory allocation bound.
