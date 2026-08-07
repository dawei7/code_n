## General
Given an integer array `ranks` and a character array `suits`. You have `5` cards where the $$i^{\text{th}}$$ card has a rank of $\text{ranks}[i]$ and a suit of $\text{suits}[i]$, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(1)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
