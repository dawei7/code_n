## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies walrus operator (`:=`) for inline assignment and zero-copy conditional check.

## Complexity detail
- **Time Complexity**: $O(n^2+m)$ — Operation count bound.
- **Space Complexity**: $O(n^2)$ — Auxiliary memory allocation bound.
