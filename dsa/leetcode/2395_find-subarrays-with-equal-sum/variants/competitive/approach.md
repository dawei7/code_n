## General
Given a **0-indexed** integer array `nums`, determine whether there exist **two** subarrays of length `2` with **equal** sum. Note that the two subarrays must begin at **different** indices, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
