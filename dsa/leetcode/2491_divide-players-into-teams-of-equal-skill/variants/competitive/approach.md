## General
Given a positive integer array `skill` of **even** length `n` where $\text{skill}[i]$ denotes the skill of the $$i^{\text{th}}$$ player. Divide the players into $n / 2$ teams of size `2` such that the total skill of each te..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
