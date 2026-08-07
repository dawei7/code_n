## General
Given an integer `n` and a **Directed Acyclic Graph (DAG)** with `n` nodes labeled from 0 to $n - 1$. This is represented by a 2D array `edges`, where $\text{edges}[i] = [u_{i}, v_{i}, w_{i}]$ indicates a directed edge from..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, a dynamic programming memoization table to cache intermediate subproblem states.

## Complexity detail
- **Time Complexity**: $O(kmt)$ — Operation count bound.
- **Space Complexity**: $O(nt)$ — Auxiliary memory allocation bound.
