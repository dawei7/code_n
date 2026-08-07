## General
Executes a SQL query for **User Activity for the Past 30 Days II** using Common Table Expressions (CTEs), GROUP BY aggregations. Edge cases: replaces NULL values using `COALESCE` guard.

## Complexity detail
- **Time Complexity**: $O(R\log R)$ — Operation count bound.
- **Space Complexity**: $O(R)$ — Auxiliary memory allocation bound.
