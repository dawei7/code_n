## General
Given two integer arrays `nums1` and `nums2`, each of length `n`. You may perform the following **split-and-merge operation** on `nums1` any number of times:, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n! * n^4)$ — Operation count bound.
- **Space Complexity**: $O(n! * n)$ — Auxiliary memory allocation bound.
