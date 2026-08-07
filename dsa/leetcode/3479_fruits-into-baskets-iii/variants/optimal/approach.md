## General
Given two arrays of integers, `fruits` and `baskets`, each of length `n`, where $\text{fruits}[i]$ represents the **quantity** of the $$i^{\text{th}}$$ type of fruit, and $\text{baskets}[j]$ represents the **capacity** of t..., the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
