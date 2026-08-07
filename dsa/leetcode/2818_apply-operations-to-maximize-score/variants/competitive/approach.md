## General
Given an array `nums` of `n` positive integers and an integer `k`, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Edge case handling: guards against empty/null inputs via early returns, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(V \log \log V + n \log n)$ — Operation count bound.
- **Space Complexity**: $O(V + n)$ — Auxiliary memory allocation bound.
