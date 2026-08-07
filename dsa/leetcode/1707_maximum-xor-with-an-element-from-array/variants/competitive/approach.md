## General
Given an array `nums` consisting of non-negative integers. You are also given a `queries` array, where $\text{queries}[i] = [x_{i}, m_{i}]$, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O((n + q)\log(n + q) + (n + q)B)$ — Operation count bound.
- **Space Complexity**: $O(nB + q)$ — Auxiliary memory allocation bound.
