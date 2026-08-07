## General
Given an integer array `groups`, where $\text{groups}[i]$ represents the size of the $$i^{\text{th}}$$ group. You are also given an integer array `elements`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(G + E + V log V)$ — Operation count bound.
- **Space Complexity**: $O(E + V)$ — Auxiliary memory allocation bound.
