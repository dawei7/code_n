## General
Given an array of `n` integers `nums`, a **132 pattern** is a subsequence of three integers $\text{nums}[i]$, $\text{nums}[j]$ and $\text{nums}[k]$ such that `i < j < k` and $\text{nums}[i] < \text{nums}[k] < \text{nums}[j]$, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
