## General
Given a string `s` and an integer `k`, return *the number of substrings in *`s`* of length *`k`* with no repeated characters*, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(\min(k, 26))$ — Auxiliary memory allocation bound.
