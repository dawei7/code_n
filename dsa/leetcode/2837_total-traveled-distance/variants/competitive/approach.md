## General
Executes a SQL query for **Total Traveled Distance** using relational JOINs, GROUP BY aggregations. Edge cases: replaces NULL values using `COALESCE` guard.

## Complexity detail
- **Time Complexity**: $O((U + R) log (U + R))$ — Operation count bound.
- **Space Complexity**: $O(U + R)$ — Auxiliary memory allocation bound.
