## General
Given a 2D integer array `orders`, where each $\text{orders}[i] = [\text{price}_{i}, \text{amount}_{i}, \text{orderType}_{i}]$ denotes that $\text{amount}_{i}$_ orders have been placed of type $\text{orderType}_{i}$ at the ..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n \log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
