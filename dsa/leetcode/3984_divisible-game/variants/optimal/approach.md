## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(U sqrt(M) + P log(P) + nP)$ — Operation count bound.
- **Space Complexity**: $O(P)$ — Auxiliary memory allocation bound.
