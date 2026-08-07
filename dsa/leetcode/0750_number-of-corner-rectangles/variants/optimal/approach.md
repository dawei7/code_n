## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed.

## Complexity detail
- **Time Complexity**: $O(mn \min(m,n))$ — Operation count bound.
- **Space Complexity**: $O(\min(m,n)^2)$ — Auxiliary memory allocation bound.
