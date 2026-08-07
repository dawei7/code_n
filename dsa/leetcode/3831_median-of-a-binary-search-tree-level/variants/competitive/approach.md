## General
Given the `root` of a **Binary Search Tree (BST)** and an integer `level`, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, binary tree node references (`val`, `left`, `right`) to traverse structural hierarchies.

## Complexity detail
- **Time Complexity**: $O(N)$ — Operation count bound.
- **Space Complexity**: $O(W)$ — Auxiliary memory allocation bound.
