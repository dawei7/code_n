## General
Given a string `s`, and an array of pairs of indices in the string `pairs` where $\text{pairs}[i] = [a, b]$ indicates 2 indices(0-indexed) of the string, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time.

## Complexity detail
- **Time Complexity**: $O((n+p)\alpha(n)+n\log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
