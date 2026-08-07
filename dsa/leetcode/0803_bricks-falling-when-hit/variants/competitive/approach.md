## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O((r \cdot c + h) \cdot \alpha(r \cdot c))$ — Operation count bound.
- **Space Complexity**: $O(r \cdot c)$ — Auxiliary memory allocation bound.
