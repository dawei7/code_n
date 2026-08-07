## General
Given There are n people in a social group labeled from `0` to $n - 1$. You are given an array `logs` where $\text{logs}[i] = [\text{timestamp}_{i}, x_{i}, y_{i}]$ indicates that $x_{i}$ and $y_{i}$ will be friends at the t..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n + m \log m + m\alpha(n))$ — Operation count bound.
- **Space Complexity**: $O(m + n)$ — Auxiliary memory allocation bound.
