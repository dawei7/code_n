## General
Given an integer `n`, return *all the structurally unique **BST'**s (binary search trees), which has exactly *`n`* nodes of unique values from* `1` *to* `n`. Return the answer in **any order**, the algorithm executes a single-pass linear scan through input elements. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends, binary tree node references (`val`, `left`, `right`) to traverse structural hierarchies. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n C_n)$ — Operation count bound.
- **Space Complexity**: $O(n C_n)$ — Auxiliary memory allocation bound.
