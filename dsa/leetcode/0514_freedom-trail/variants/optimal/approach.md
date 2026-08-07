## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed.

## Complexity detail
- **Time Complexity**: $O(|ring| \cdot |key|)$ — Operation count bound.
- **Space Complexity**: $O(|ring|)$ — Auxiliary memory allocation bound.
