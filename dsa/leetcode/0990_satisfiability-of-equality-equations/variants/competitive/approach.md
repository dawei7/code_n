## General
Given an array of strings `equations` that represent relationships between variables where each string $\text{equations}[i]$ is of length `4` and takes one of two different forms: $"x_{i} = y_{i}"$ or $"x_{i}\neq y_{i}"$.He..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(Q\alpha(26))$ — Operation count bound.
- **Space Complexity**: $O(26)$ — Auxiliary memory allocation bound.
