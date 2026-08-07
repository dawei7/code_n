## General
Given an integer `n`. A perfectly straight street is represented by a number line ranging from `0` to $n - 1$. You are given a 2D integer array `lights` representing the street lamp(s) on the street. Each $\text{lights}[i] ..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n + m)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
