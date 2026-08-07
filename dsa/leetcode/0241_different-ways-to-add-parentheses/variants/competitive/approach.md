## General
Given a string `expression` of numbers and operators, return *all possible results from computing all the different possible ways to group numbers and operators*. You may return the answer in **any order**, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(C_n \cdot n)$ — Operation count bound.
- **Space Complexity**: $O(C_n \cdot n)$ — Auxiliary memory allocation bound.
