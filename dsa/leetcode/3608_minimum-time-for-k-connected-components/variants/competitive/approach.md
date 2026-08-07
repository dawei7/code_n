## General
Given an integer `n` and an undirected graph with `n` nodes labeled from 0 to $n - 1$. This is represented by a 2D array `edges`, where $\text{edges}[i] = [u_{i}, v_{i}, \text{time}_{i}]$ indicates an undirected edge betwee..., the algorithm executes a single-pass linear scan through input elements. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(m log m + (n + m) \alpha(n))$ — Operation count bound.
- **Space Complexity**: $O(n + m)$ — Auxiliary memory allocation bound.
