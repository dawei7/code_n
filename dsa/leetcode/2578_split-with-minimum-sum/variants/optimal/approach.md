## General
Given a positive integer `num`, split it into two non-negative integers `num1` and `num2` such that:, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(d log d)$ — Operation count bound.
- **Space Complexity**: $O(d)$ — Auxiliary memory allocation bound.
