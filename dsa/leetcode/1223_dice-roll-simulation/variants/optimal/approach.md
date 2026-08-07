## General
Given A die simulator generates a random number from `1` to `6` for each roll. You introduced a constraint to the generator such that it cannot roll the number `i` more than $\text{rollMax}[i]$ (**1-indexed**) consecutive t..., the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(nR)$ — Operation count bound.
- **Space Complexity**: $O(R)$ — Auxiliary memory allocation bound.
