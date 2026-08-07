## General
Given an array of `intervals` where $\text{intervals}[i] = [\text{start}_{i}, \text{end}_{i}]$, merge all overlapping intervals, and return *an array of the non-overlapping intervals that cover all the intervals in the input*, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n \log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
