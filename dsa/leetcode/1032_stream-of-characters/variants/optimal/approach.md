## General
Given Design an algorithm that accepts a stream of characters and checks if a suffix of these characters is a string of a given array of strings `words`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(S+QW)$ — Operation count bound.
- **Space Complexity**: $O(S+W)$ — Auxiliary memory allocation bound.
