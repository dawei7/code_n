## General
Executes a SQL query for **The Category of Each Member in the Store** using Common Table Expressions (CTEs), relational JOINs, GROUP BY aggregations. Edge cases: replaces NULL values using `COALESCE` guard.

## Complexity detail
- **Time Complexity**: $O(M+V+P)$ — Operation count bound.
- **Space Complexity**: $O(M+V+P)$ — Auxiliary memory allocation bound.
