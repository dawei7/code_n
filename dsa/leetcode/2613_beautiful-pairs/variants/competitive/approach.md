## General
Given two **0-indexed** integer arrays `nums1` and `nums2` of the same length. A pair of indices `(i,j)` is called **beautiful** if$|\text{nums1}[i] - \text{nums1}[j]| + |\text{nums2}[i] - \text{nums2}[j]|$ is the smallest ..., the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n\log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
