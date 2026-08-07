## General
Given ![](images/cinema_seats_1.png), the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(r)$ — Operation count bound.
- **Space Complexity**: $O(min(n,r))$ — Auxiliary memory allocation bound.
