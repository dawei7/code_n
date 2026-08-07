## General
Given an array of positive integers `nums`, return *the number of **distinct prime factors** in the product of the elements of* `nums`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n sqrt M)$ — Operation count bound.
- **Space Complexity**: $O(p)$ — Auxiliary memory allocation bound.
