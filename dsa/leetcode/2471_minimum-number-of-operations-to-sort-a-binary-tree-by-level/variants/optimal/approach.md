## General
Given the `root` of a binary tree with **unique values**, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends, binary tree node references (`val`, `left`, `right`) to traverse structural hierarchies.

## Complexity detail
- **Time Complexity**: $O(n log W)$ — Operation count bound.
- **Space Complexity**: $O(W)$ — Auxiliary memory allocation bound.
