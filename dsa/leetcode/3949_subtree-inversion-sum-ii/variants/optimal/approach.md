## General
Given an undirected tree rooted at node 0, with `n` nodes numbered from 0 to $n - 1$. The tree is represented by a 2D integer array `edges` of length $n - 1$, where $\text{edges}[i] = [u_{i}, v_{i}]$ indicates an edge betwe..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(nk)$ — Operation count bound.
- **Space Complexity**: $O(nk)$ — Auxiliary memory allocation bound.
