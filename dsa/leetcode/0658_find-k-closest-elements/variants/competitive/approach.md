## General
Given a **sorted** integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order, the algorithm executes binary search over the search space to achieve logarithmic reduction.

## Complexity detail
- **Time Complexity**: $O(\log(N - K) + K)$ — Operation count bound.
- **Space Complexity**: $O(K)$ — Auxiliary memory allocation bound.
