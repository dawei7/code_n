## General
Given an `m x n` `matrix`, return *a new matrix *`answer`* where *$\text{answer}[row][col]$* is the ****rank** of *$\text{matrix}[row][col]$, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(V\log V)$ — Operation count bound.
- **Space Complexity**: $O(V)$ — Auxiliary memory allocation bound.
