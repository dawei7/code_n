## General
Given There is a tree (i.e. a connected, undirected graph with no cycles) consisting of `n` nodes numbered from `0` to $n - 1$ and exactly $n - 1$ edges, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
