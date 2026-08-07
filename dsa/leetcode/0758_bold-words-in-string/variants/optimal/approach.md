## General
Given an array of keywords `words` and a string `s`, make all appearances of all keywords $\text{words}[i]$ in `s` bold. Any letters between `<b>` and `</b>` tags become bold, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(p + nL)$ — Operation count bound.
- **Space Complexity**: $O(p + n)$ — Auxiliary memory allocation bound.
