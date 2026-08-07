## General
Given a **0-indexed** integer array `nums`. There exists an array `arr` of length `nums.length`, where $\text{arr}[i]$ is the sum of $|i - j|$ over all `j` such that $\text{nums}[j] = \text{nums}[i]$ and $j \neq i$. If ther..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
