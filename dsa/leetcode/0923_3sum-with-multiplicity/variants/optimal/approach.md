## General
Given an integer array `arr`, and an integer `target`, return the number of tuples `i, j, k` such that `i < j < k` and $\text{arr}[i] + \text{arr}[j] + \text{arr}[k] = target$, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n+V^2)$ — Operation count bound.
- **Space Complexity**: $O(V)$ — Auxiliary memory allocation bound.
