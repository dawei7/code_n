## General
Executes a SQL query for **Top Travellers** using relational JOINs. Edge cases: replaces NULL values using `COALESCE` guard.

## Complexity detail
- **Time Complexity**: $O(U + R + U\log U)$ — Operation count bound.
- **Space Complexity**: $O(U)$ — Auxiliary memory allocation bound.
