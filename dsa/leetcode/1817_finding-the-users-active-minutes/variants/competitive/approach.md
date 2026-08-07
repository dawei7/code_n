## General
Given the logs for users' actions on LeetCode, and an integer `k`. The logs are represented by a 2D integer array `logs` where each $\text{logs}[i] = [\text{ID}_{i}, \text{time}_{i}]$ indicates that the user with $\text{ID}..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n + k)$ — Operation count bound.
- **Space Complexity**: $O(n + k)$ — Auxiliary memory allocation bound.
