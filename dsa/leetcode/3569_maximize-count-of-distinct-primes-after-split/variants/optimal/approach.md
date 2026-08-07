## General
Given an integer array `nums` having length `n` and a 2D integer array `queries` where $\text{queries}[i] = [idx, val]$, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(U log log U + (n + q) log(n + q))$ — Operation count bound.
- **Space Complexity**: $O(U + n + q)$ — Auxiliary memory allocation bound.
