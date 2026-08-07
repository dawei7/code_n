## General
Given a **0-indexed** $m * n$ integer matrix `values`, representing the values of $m * n$ different items in `m` different shops. Each shop has `n` items where the $$j^{\text{th}}$$ item in the $$i^{\text{th}}$$ shop has a ..., the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O(m n log(m))$ — Operation count bound.
- **Space Complexity**: $O(m)$ — Auxiliary memory allocation bound.
