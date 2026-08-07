## General
Given an integer array `nums` and an integer `k`, return *the maximum length of a **subarray** that sums to* `k`. If there is not one, return `0` instead, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
