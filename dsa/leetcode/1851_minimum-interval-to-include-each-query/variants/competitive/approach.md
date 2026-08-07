## General
Given a 2D integer array `intervals`, where $\text{intervals}[i] = [\text{left}_{i}, \text{right}_{i}]$ describes the $$i^{\text{th}}$$ interval starting at $\text{left}_{i}$ and ending at $\text{right}_{i}$ **(inclusive)**..., the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O((n+q)\log(n+q))$ — Operation count bound.
- **Space Complexity**: $O(n+q)$ — Auxiliary memory allocation bound.
