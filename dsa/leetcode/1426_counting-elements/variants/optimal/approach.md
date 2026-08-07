## General
Given an integer array `arr`, count how many elements `x` there are, such that $x + 1$ is also in `arr`. If there are duplicates in `arr`, count them separately, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
