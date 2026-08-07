## General
Given an array representing a row of `seats` where $\text{seats}[i] = 1$ represents a person sitting in the $$i^{\text{th}}$$ seat, and $\text{seats}[i] = 0$ represents that the $$i^{\text{th}}$$ seat is empty **(0-indexed)**, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
