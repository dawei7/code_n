## General
Given There are `n` houses in a village. We want to supply water for all the houses by building wells and laying pipes, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(e \log e)$ — Operation count bound.
- **Space Complexity**: $O(e)$ — Auxiliary memory allocation bound.
