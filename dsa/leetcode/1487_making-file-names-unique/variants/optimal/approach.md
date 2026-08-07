## General
Given an array of strings `names` of size `n`. You will create `n` folders in your file system **such that**, at the $$i^{\text{th}}$$ minute, you will create a folder with the name $\text{names}[i]$, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(N)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
