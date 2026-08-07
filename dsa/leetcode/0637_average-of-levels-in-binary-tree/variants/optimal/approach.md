## General
Given the `root` of a binary tree, return *the average value of the nodes on each level in the form of an array*. Answers within $10^{-5}$ of the actual answer will be accepted, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends, binary tree node references (`val`, `left`, `right`) to traverse structural hierarchies.

## Complexity detail
- **Time Complexity**: $O(N)$ — Operation count bound.
- **Space Complexity**: $O(W)$ — Auxiliary memory allocation bound.
