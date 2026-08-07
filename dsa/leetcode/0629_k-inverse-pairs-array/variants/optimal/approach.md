## General
Given For an integer array `nums`, an **inverse pair** is a pair of integers `[i, j]` where $0 \le i < j < \text{nums.length}$ and $\text{nums}[i] > \text{nums}[j]$, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(nk)$ — Operation count bound.
- **Space Complexity**: $O(k)$ — Auxiliary memory allocation bound.
