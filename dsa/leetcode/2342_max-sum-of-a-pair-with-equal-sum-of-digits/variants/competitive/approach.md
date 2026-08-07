## General
Given a **0-indexed** array `nums` consisting of **positive** integers. You can choose two indices `i` and `j`, such that $i \neq j$, and the sum of digits of the number $\text{nums}[i]$ is equal to that of $\text{nums}[j]$, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
