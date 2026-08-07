## General
Given a positive integer `p`. Consider an array `nums` (**1-indexed**) that consists of the integers in the **inclusive** range $[1, 2^p - 1]$ in their binary representations. You are allowed to do the following operation *..., the algorithm solves **Minimum Non-Zero Product of the Array Elements** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(p)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
