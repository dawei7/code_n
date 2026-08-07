## General
Given two integers, `n` and `threshold`, as well as a **directed** weighted graph of `n` nodes numbered from 0 to $n - 1$. The graph is represented by a **2D** integer array `edges`, where $\text{edges}[i] = [A_{i}, B_{i}, ..., the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O((n + m) \log n)$ — Operation count bound.
- **Space Complexity**: $O(n + m)$ — Auxiliary memory allocation bound.
