## General
Executes a SQL query for **User Purchase Platform** using relational JOINs. Edge cases: replaces NULL values using `COALESCE` guard, filters aggregated group boundaries using `HAVING` clause.

## Complexity detail
- **Time Complexity**: $O(R \log R)$ — Operation count bound.
- **Space Complexity**: $O(R)$ — Auxiliary memory allocation bound.
