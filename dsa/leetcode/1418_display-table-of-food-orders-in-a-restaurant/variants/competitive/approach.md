## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed.

## Complexity detail
- **Time Complexity**: $O(N + F\log F + T\log T + TF)$ — Operation count bound.
- **Space Complexity**: $O(N + TF)$ — Auxiliary memory allocation bound.
