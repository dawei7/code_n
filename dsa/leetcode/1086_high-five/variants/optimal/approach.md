## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies walrus operator (`:=`) for inline assignment and zero-copy conditional check.

## Complexity detail
- **Time Complexity**: $O(N+S\log S)$ — Operation count bound.
- **Space Complexity**: $O(S)$ — Auxiliary memory allocation bound.
