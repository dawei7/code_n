## General
Given a **0-indexed** array of strings `nums`, where each string is of **equal length** and consists of only digits, the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(nL + q)$ — Operation count bound.
- **Space Complexity**: $O(n + q)$ — Auxiliary memory allocation bound.
