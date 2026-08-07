## General
Given two integer arrays, `source` and `target`, both of length `n`. You are also given an array `allowedSwaps` where each $\text{allowedSwaps}[i] = [a_{i}, b_{i}]$ indicates that you are allowed to swap the elements at ind..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O((n+m)\alpha(n))$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
