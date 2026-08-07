## General
Given a **0-indexed** array of positive integers `nums`. A triplet of three **distinct** indices `(i, j, k)` is called a **single divisor triplet** of `nums` if $\text{nums}[i] + \text{nums}[j] + \text{nums}[k]$ is divisibl..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n + U^3)$ — Operation count bound.
- **Space Complexity**: $O(U)$ — Auxiliary memory allocation bound.
