## General
Given a tree with `n` nodes numbered from `0` to $n - 1$ in the form of a parent array `parent` where $\text{parent}[i]$ is the parent of the $$i^{\text{th}}$$ node. The root of the tree is node `0`, so $\text{parent}[0] = ..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(N)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
