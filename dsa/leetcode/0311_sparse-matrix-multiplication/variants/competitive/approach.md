## General
Given two <a href="https://en.wikipedia.org/wiki/Sparse_matrix" target="_blank">sparse matrices</a> `mat1` of size `m x k` and `mat2` of size `k x n`, return the result of `mat1 x mat2`. You may assume that multiplication i..., the algorithm executes a single-pass linear scan through input elements.

## Complexity detail
- **Time Complexity**: $O(mk + kn + z)$ — Operation count bound.
- **Space Complexity**: $O(kn)$ — Auxiliary memory allocation bound.
