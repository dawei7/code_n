## General
Given an array of meeting time intervals `intervals` where $\text{intervals}[i] = [\text{start}_{i}, \text{end}_{i}]$, return *the minimum number of conference rooms required*, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n \log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
