## General
Given a list of `preferences` for `n` friends, where `n` is always **even**, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(N^2)$ — Operation count bound.
- **Space Complexity**: $O(N^2)$ — Auxiliary memory allocation bound.
