## General
Given a 2D `matrix` of size `m x n`, consisting of non-negative integers. You are also given an integer `k`, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(C\log k)$ — Operation count bound.
- **Space Complexity**: $O(n+k)$ — Auxiliary memory allocation bound.
