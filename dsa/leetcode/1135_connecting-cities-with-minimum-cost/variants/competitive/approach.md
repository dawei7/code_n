## General
Given There are `n` cities labeled from `1` to `n`. You are given the integer `n` and an array `connections` where $\text{connections}[i] = [x_{i}, y_{i}, \text{cost}_{i}]$ indicates that the cost of connecting city $x_{i}$..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n + m\log m)$ — Operation count bound.
- **Space Complexity**: $O(n + m)$ — Auxiliary memory allocation bound.
