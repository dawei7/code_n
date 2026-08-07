## General
Given There exists an undirected and unrooted tree with `n` nodes indexed from `0` to $n - 1$. You are given an integer `n` and a 2D integer array edges of length $n - 1$, where $\text{edges}[i] = [a_{i}, b_{i}]$ indicates ..., the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
