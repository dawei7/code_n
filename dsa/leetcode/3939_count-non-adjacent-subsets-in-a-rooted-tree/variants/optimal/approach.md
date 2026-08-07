## General
Given a rooted tree with `n` nodes labeled from 0 to $n - 1$, represented by an integer array `parent` of length `n`, where:, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(NK^2)$ — Operation count bound.
- **Space Complexity**: $O(NK)$ — Auxiliary memory allocation bound.
