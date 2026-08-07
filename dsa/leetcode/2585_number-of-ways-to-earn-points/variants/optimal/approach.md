## General
Given There is a test that has `n` types of questions. You are given an integer `target` and a **0-indexed** 2D integer array `types` where $\text{types}[i] = [\text{count}_{i}, \text{marks}_{i}]$ indicates that there are $..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n * target)$ — Operation count bound.
- **Space Complexity**: $O(target)$ — Auxiliary memory allocation bound.
