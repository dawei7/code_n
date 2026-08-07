## General
Given an `m x n` `board` of characters and a list of strings `words`, return *all words on the board*, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(mn4^L)$ — Operation count bound.
- **Space Complexity**: $O(T + L)$ — Auxiliary memory allocation bound.
