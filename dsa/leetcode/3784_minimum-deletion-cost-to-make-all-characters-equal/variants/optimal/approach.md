## General
Given a string `s` of length `n` and an integer array `cost` of the same length, where $\text{cost}[i]$ is the cost to **delete** the $$i^{\text{th}}$$ character of `s`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(N)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
