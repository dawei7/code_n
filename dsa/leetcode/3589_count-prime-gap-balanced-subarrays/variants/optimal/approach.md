## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed, double-ended queue (`deque`) for $O(1)$ window bounds.

## Complexity detail
- **Time Complexity**: $O(V log log V + n)$ — Operation count bound.
- **Space Complexity**: $O(V + n)$ — Auxiliary memory allocation bound.
