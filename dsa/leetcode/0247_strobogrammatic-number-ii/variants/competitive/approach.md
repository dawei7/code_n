## General
Given an integer `n`, return all the **strobogrammatic numbers** that are of length `n`. You may return the answer in **any order**, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n \cdot 5^{n/2})$ — Operation count bound.
- **Space Complexity**: $O(n \cdot 5^{n/2})$ — Auxiliary memory allocation bound.
