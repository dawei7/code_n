## General
Given the strings `s1` and `s2` of size `n` and the string `evil`, return *the number of **good** strings*, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(26nm)$ — Operation count bound.
- **Space Complexity**: $O(nm)$ — Auxiliary memory allocation bound.
