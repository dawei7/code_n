## General
Given an array of `events` where $\text{events}[i] = [\text{startDay}_{i}, \text{endDay}_{i}]$. Every event `i` starts at $\text{startDay}_{i}$_ and ends at $\text{endDay}_{i}$, the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n \log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
