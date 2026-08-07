## General
Given `n` **BST (binary search tree) root nodes** for `n` separate BSTs stored in an array `trees` (**0-indexed**). Each BST in `trees` has **at most 3 nodes**, and no two roots have the same value. In one operation, you can:, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(T)$ — Operation count bound.
- **Space Complexity**: $O(K+H)$ — Auxiliary memory allocation bound.
