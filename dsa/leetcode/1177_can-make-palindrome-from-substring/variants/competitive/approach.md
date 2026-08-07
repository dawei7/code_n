## General
Given a string `s` and array `queries` where $\text{queries}[i] = [\text{left}_{i}, \text{right}_{i}, k_{i}]$. We may rearrange the substring $s[\text{left}_{i}...\text{right}_{i}]$ for each query and then choose up to $k_{..., the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n+q)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
