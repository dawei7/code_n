## General
Executes a SQL query for **Product Price at a Given Date** using Common Table Expressions (CTEs), relational JOINs, GROUP BY aggregations. Edge cases: replaces NULL values using `COALESCE` guard.

## Complexity detail
- **Time Complexity**: $O(r \log r)$ — Operation count bound.
- **Space Complexity**: $O(r)$ — Auxiliary memory allocation bound.
