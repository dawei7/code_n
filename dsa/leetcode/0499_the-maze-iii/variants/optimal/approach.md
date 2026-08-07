## General
Algorithm uses two-pointer sliding window iteration. Maintains double-ended queue (`deque`) for $O(1)$ window bounds.

## Complexity detail
- **Time Complexity**: $O(rows \cdot cols \cdot p \log(rows \cdot cols))$ — Operation count bound.
- **Space Complexity**: $O(rows \cdot cols \cdot p)$ — Auxiliary memory allocation bound.
