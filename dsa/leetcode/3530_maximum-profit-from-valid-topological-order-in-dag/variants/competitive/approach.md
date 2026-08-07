## General
Given a **Directed Acyclic Graph (DAG)** with `n` nodes labeled from `0` to $n - 1$, represented by a 2D array `edges`, where $\text{edges}[i] = [u_{i}, v_{i}]$ indicates a directed edge from node $u_{i}$ to $v_{i}$. Each n..., the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n * 2^n)$ — Operation count bound.
- **Space Complexity**: $O(2^n)$ — Auxiliary memory allocation bound.
