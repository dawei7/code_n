## General
Given a `pattern` and a string `s`, return `true`* if *`s`* **matches** the *`pattern`*.*, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n \cdot 2^n)$ — Operation count bound.
- **Space Complexity**: $O(n + p)$ — Auxiliary memory allocation bound.
