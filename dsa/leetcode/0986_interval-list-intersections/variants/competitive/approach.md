## General
Given two lists of closed intervals, `firstList` and `secondList`, where $\text{firstList}[i] = [\text{start}_{i}, \text{end}_{i}]$ and $\text{secondList}[j] = [\text{start}_{j}, \text{end}_{j}]$. Each list of intervals is ..., the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(M+N)$ — Operation count bound.
- **Space Complexity**: $O(K)$ — Auxiliary memory allocation bound.
