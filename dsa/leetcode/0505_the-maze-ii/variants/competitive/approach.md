## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed, hash set (`set`) for $O(1)$ duplicate check, priority queue (`heapq`) for dynamic ordering.

## Complexity detail
- **Time Complexity**: $O(rows \cdot cols \log(rows \cdot cols))$ — Operation count bound.
- **Space Complexity**: $O(rows \cdot cols)$ — Auxiliary memory allocation bound.
