## General
Executes a SQL query for **Exchange Seats** using relational JOINs. Edge cases: replaces NULL values using `COALESCE` guard.

## Complexity detail
- **Time Complexity**: $O(R \log R)$ — Operation count bound.
- **Space Complexity**: $O(R)$ — Auxiliary memory allocation bound.
