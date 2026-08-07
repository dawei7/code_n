## General
Given an integer `n`, representing `n` nodes numbered from 0 to $n - 1$ and a list of `edges`, where $\text{edges}[i] = [u_{i}, v_{i}, s_{i}, \text{must}_{i}]$:, the algorithm executes a single-pass linear scan through input elements. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(m log m)$ — Operation count bound.
- **Space Complexity**: $O(n + m)$ — Auxiliary memory allocation bound.
