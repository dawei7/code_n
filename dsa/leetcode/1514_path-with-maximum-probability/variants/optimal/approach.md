## General
Given an undirected weighted graph of `n` nodes (0-indexed), represented by an edge list where $\text{edges}[i] = [a, b]$ is an undirected edge connecting the nodes `a` and `b` with a probability of success of traversing th..., the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Key operations include the walrus operator (`:=`) for inline assignment and evaluation.

## Complexity detail
- **Time Complexity**: $O((n+e)\log n)$ — Operation count bound.
- **Space Complexity**: $O(n+e)$ — Auxiliary memory allocation bound.
