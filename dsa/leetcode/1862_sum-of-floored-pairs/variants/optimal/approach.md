## General
Given an integer array `nums`, return the sum of $floor(\text{nums}[i] / \text{nums}[j])$ for all pairs of indices $0 \le i, j < \text{nums.length}$ in the array. Since the answer may be too large, return it **modulo** $10^..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n + U\log U)$ — Operation count bound.
- **Space Complexity**: $O(U)$ — Auxiliary memory allocation bound.
