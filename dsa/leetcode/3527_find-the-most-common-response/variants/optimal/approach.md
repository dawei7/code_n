## General
Given a 2D string array `responses` where each $\text{responses}[i]$ is an array of strings representing survey responses from the $$i^{\text{th}}$$ day, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(S)$ — Operation count bound.
- **Space Complexity**: $O(U)$ — Auxiliary memory allocation bound.
