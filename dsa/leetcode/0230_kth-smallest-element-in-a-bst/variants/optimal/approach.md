## General
Given the `root` of a binary search tree, and an integer `k`, return *the* $$k^{\text{th}}$$ *smallest value (**1-indexed**) of all the values of the nodes in the tree*, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes binary tree node references (`val`, `left`, `right`) to traverse structural hierarchies.

## Complexity detail
- **Time Complexity**: $O(h + k)$ — Operation count bound.
- **Space Complexity**: $O(h)$ — Auxiliary memory allocation bound.
