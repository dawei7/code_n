## General
Given a binary tree where each path going from the root to any leaf form a **valid sequence**, check if a given string is a **valid sequence** in such binary tree, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes binary tree node references (`val`, `left`, `right`) to traverse structural hierarchies. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(N)$ — Operation count bound.
- **Space Complexity**: $O(h)$ — Auxiliary memory allocation bound.
