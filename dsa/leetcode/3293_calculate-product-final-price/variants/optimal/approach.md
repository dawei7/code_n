## General
Executes a SQL query for **Calculate Product Final Price** using relational JOINs. Edge cases: replaces NULL values using `COALESCE` guard.

## Complexity detail
- **Time Complexity**: $O((P + D) log(P + D))$ — Operation count bound.
- **Space Complexity**: $O(P + D)$ — Auxiliary memory allocation bound.
