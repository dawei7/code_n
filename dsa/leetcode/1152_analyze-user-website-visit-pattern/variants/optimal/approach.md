## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed, hash set (`set`) for $O(1)$ duplicate check.

## Complexity detail
- **Time Complexity**: $O(m \log m + C)$ — Operation count bound.
- **Space Complexity**: $O(m + C)$ — Auxiliary memory allocation bound.
