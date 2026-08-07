## General
Given two **0-indexed** binary arrays `nums1` and `nums2`. Find the **widest** pair of indices `(i, j)` such that $i \le j$ and $\text{nums1}[i] + nums1[i+1] + ... + \text{nums1}[j] = \text{nums2}[i] + nums2[i+1] + ... + \t..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(N)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
