## General
Given an array of strings `words` (**without duplicates**), return *all the **concatenated words** in the given list of* `words`, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(sum(|word|^2))$ — Operation count bound.
- **Space Complexity**: $O(sum(|word|))$ — Auxiliary memory allocation bound.
