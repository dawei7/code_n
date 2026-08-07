## General
Given A bus has `n` stops numbered from `0` to $n - 1$ that form a circle. We know the distance between all pairs of neighboring stops where $\text{distance}[i]$ is the distance between the stops number `i` and $(i + 1) \% n$, the algorithm solves **Distance Between Bus Stops** directly. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
