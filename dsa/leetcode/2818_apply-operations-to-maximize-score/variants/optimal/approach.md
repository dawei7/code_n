## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed, hash set (`set`) for $O(1)$ duplicate check. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(V \log \log V + n \log n)$ — Operation count bound.
- **Space Complexity**: $O(V + n)$ — Auxiliary memory allocation bound.
