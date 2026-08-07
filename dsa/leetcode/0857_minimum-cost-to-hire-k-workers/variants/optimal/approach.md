## General
Given There are `n` workers. You are given two integer arrays `quality` and `wage` where $\text{quality}[i]$ is the quality of the $$i^{\text{th}}$$ worker and $\text{wage}[i]$ is the minimum wage expectation for the $$i^{\..., the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n\log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
