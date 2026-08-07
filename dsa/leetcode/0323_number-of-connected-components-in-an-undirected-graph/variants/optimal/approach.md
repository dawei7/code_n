## General
Given You have a graph of `n` nodes. You are given an integer `n` and an array `edges` where $\text{edges}[i] = [a_{i}, b_{i}]$ indicates that there is an edge between $a_{i}$ and $b_{i}$ in the graph, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time.

## Complexity detail
- **Time Complexity**: $O(n + e \alpha(n))$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
