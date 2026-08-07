## General
Given a list of `dominoes`, $\text{dominoes}[i] = [a, b]$ is **equivalent to** $\text{dominoes}[j] = [c, d]$ if and only if either ($a = c$ and $b = d$), or ($a = d$ and $b = c$) - that is, one domino can be rotated to be e..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
