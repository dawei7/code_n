## General
Given In a special ranking system, each voter gives a rank from highest to lowest to all teams participating in the competition, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(VT+T^2\log T)$ — Operation count bound.
- **Space Complexity**: $O(T^2)$ — Auxiliary memory allocation bound.
