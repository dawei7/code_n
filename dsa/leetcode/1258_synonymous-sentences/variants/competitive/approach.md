## General
Given a list of equivalent string pairs `synonyms` where $\text{synonyms}[i] = [s_{i}, t_{i}]$ indicates that $s_{i}$ and $t_{i}$ are equivalent strings. You are also given a sentence `text`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(P\alpha(V)+V\log V+KW)$ — Operation count bound.
- **Space Complexity**: $O(V+KW)$ — Auxiliary memory allocation bound.
