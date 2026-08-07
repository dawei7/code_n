## General
Given a string `s` and an array of strings `words`, return *the number of* $\text{words}[i]$ *that is a subsequence of* `s`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(S + L)$ — Operation count bound.
- **Space Complexity**: $O(W)$ — Auxiliary memory allocation bound.
