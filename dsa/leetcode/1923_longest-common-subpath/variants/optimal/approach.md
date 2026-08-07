## General
Given There is a country of `n` cities numbered from `0` to $n - 1$. In this country, there is a road connecting **every pair** of cities, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(T \log L)$ — Operation count bound.
- **Space Complexity**: $O(T)$ — Auxiliary memory allocation bound.
