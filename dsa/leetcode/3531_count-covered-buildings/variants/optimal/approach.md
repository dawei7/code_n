## General
Given a positive integer `n`, representing an `n x n` city. You are also given a 2D grid `buildings`, where $\text{buildings}[i] = [x, y]$ denotes a **unique** building located at coordinates `[x, y]`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(B)$ — Operation count bound.
- **Space Complexity**: $O(B)$ — Auxiliary memory allocation bound.
