## General
Given an array of `events` where $\text{events}[i] = [\text{startDay}_{i}, \text{endDay}_{i}]$. Every event `i` starts at $\text{startDay}_{i}$_ and ends at $\text{endDay}_{i}$, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O(n \log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
