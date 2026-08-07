## General
Given an integer array `nums`. This array contains `n` elements, where **exactly** $n - 2$ elements are **special**** numbers**. One of the remaining **two** elements is the *sum* of these **special numbers**, and the other..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
