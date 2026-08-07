## General
Given an integer array of even length `arr`, return `true`* if it is possible to reorder *`arr`* such that *$arr[2 * i + 1] = 2 * arr[2 * i]$* for every *$0 \le i < len(arr) / 2$*, or *`false`* otherwise*, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(N\log N)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
