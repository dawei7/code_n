## General
Given an array of integer arrays `arrays` where each $\text{arrays}[i]$ is sorted in **strictly increasing** order, return *an integer array representing the **longest common subsequence** among **all** the arrays*, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(T+V)$ — Operation count bound.
- **Space Complexity**: $O(V)$ — Auxiliary memory allocation bound.
