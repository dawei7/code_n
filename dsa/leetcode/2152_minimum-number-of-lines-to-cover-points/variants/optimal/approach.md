## General
Given an array `points` where $\text{points}[i] = [x_{i}, y_{i}]$ represents a point on an **X-Y **plane, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n^3 + n * 2^n)$ — Operation count bound.
- **Space Complexity**: $O(n^2 + 2^n)$ — Auxiliary memory allocation bound.
