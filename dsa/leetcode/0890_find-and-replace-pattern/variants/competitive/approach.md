## General
Given a list of strings `words` and a string `pattern`, return *a list of* $\text{words}[i]$ *that match* `pattern`. You may return the answer in **any order**, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(NL)$ — Operation count bound.
- **Space Complexity**: $O(N+L)$ — Auxiliary memory allocation bound.
