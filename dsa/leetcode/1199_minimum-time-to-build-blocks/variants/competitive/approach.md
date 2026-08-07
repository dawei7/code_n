## General
Given a list of blocks, where $\text{blocks}[i] = t$ means that the `i`-th block needs `t` units of time to be built. A block can only be built by exactly one worker, the algorithm solves **Minimum Time to Build Blocks** directly. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O(n\log n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
