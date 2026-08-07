## General
Given We can represent a sentence as an array of words, for example, the sentence `"I am happy with leetcode"` can be represented as `arr = ["I","am",happy","with","leetcode"]`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O((n+p) \alpha(w))$ — Operation count bound.
- **Space Complexity**: $O(w)$ — Auxiliary memory allocation bound.
