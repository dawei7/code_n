## General
Given two strings `order` and `s`. All the characters of `order` are **unique** and were sorted in some custom order previously, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(m + n)$ — Operation count bound.
- **Space Complexity**: $O(u)$ — Auxiliary memory allocation bound.
