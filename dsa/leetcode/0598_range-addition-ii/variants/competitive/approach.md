## General
Given an `m x n` matrix `M` initialized with all `0`'s and an array of operations `ops`, where $\text{ops}[i] = [a_{i}, b_{i}]$ means $M[x][y]$ should be incremented by one for all $0 \le x < a_{i}$ and $0 \le y < b_{i}$, the algorithm executes a single-pass linear scan through input elements.

## Complexity detail
- **Time Complexity**: $O(k)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
