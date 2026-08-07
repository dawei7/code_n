## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies walrus operator (`:=`) for inline assignment and zero-copy conditional check. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(N+K)$ — Operation count bound.
- **Space Complexity**: $O(K)$ — Auxiliary memory allocation bound.
