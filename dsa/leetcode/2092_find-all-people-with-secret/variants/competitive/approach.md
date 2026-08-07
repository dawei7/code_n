## General
Given an integer `n` indicating there are `n` people numbered from `0` to $n - 1$. You are also given a **0-indexed** 2D integer array `meetings` where $\text{meetings}[i] = [x_{i}, y_{i}, \text{time}_{i}]$ indicates that p..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time.

## Complexity detail
- **Time Complexity**: $O(M \log M + n)$ — Operation count bound.
- **Space Complexity**: $O(M+n)$ — Auxiliary memory allocation bound.
