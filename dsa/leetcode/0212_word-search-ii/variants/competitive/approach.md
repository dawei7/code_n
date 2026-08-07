## General
Given an `m x n` `board` of characters and a list of strings `words`, return *all words on the board*, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(mn4^L)$ — Operation count bound.
- **Space Complexity**: $O(T + L)$ — Auxiliary memory allocation bound.
