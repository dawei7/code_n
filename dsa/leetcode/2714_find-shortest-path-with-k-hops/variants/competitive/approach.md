## General
Given a positive integer `n` which is the number of nodes of a **0-indexed undirected weighted connected** graph and a **0-indexed** **2D array** `edges` where $\text{edges}[i] = [u_{i}, v_{i}, w_{i}]$ indicates that there ..., the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O(E*(K+1)*log(n*(K+1)))$ — Operation count bound.
- **Space Complexity**: $O((n+E)*(K+1))$ — Auxiliary memory allocation bound.
