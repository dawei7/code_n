## General
Given a `rows x cols` screen and a `sentence` represented as a list of strings, return *the number of times the given sentence can be fitted on the screen*, the algorithm executes a single-pass linear scan through input elements. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(\min(r,L)w)$ — Operation count bound.
- **Space Complexity**: $O(L)$ — Auxiliary memory allocation bound.
