## General
Given We have an array of integers, `nums`, and an array of `requests` where $\text{requests}[i] = [\text{start}_{i}, \text{end}_{i}]$. The $$i^{\text{th}}$$ request asks for the sum of $nums[\text{start}_{i}] + nums[\text{..., the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(N\log N+R)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
