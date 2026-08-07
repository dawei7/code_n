## General
Given a** directed acyclic graph**, with `n` vertices numbered from `0` to `n-1`, and an array `edges` where $\text{edges}[i] = [\text{from}_{i}, \text{to}_{i}]$ represents a directed edge from node $\text{from}_{i}$ to nod..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time.

## Complexity detail
- **Time Complexity**: $O(n+M)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
