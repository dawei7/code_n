## General
Given There is a group of `n` members, and a list of various crimes they could commit. The $$i^{\text{th}}$$ crime generates a $\text{profit}[i]$ and requires $\text{group}[i]$ members to participate in it. If a member part..., the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(mn(P+1))$ — Operation count bound.
- **Space Complexity**: $O(n(P+1))$ — Auxiliary memory allocation bound.
