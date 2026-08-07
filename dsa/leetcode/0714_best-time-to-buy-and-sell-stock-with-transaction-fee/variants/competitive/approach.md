## General
Given an array `prices` where $\text{prices}[i]$ is the price of a given stock on the $$i^{\text{th}}$$ day, and an integer `fee` representing a transaction fee, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
