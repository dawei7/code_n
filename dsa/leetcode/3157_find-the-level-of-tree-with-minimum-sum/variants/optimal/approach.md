## General
Given the root of a binary tree `root` where each node has a value, return the level of the tree that has the **minimum** sum of values among all the levels (in case of a tie, return the **lowest** level), the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends, binary tree node references (`val`, `left`, `right`) to traverse structural hierarchies.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
