## General
Given There is an exam room with `n` seats in a single row labeled from `0` to $n - 1$, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O(q\log q)$ — Operation count bound.
- **Space Complexity**: $O(q)$ — Auxiliary memory allocation bound.
