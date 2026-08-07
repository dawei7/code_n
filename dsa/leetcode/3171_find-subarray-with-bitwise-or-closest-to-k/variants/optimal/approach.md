## General
Given an array `nums` and an integer `k`. You need to find a subarray of `nums` such that the **absolute difference** between `k` and the bitwise `OR` of the subarray elements is as** small** as possible. In other words, se..., the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n log M)$ — Operation count bound.
- **Space Complexity**: $O(log M)$ — Auxiliary memory allocation bound.
