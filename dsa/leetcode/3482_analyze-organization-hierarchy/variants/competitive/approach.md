## General
Executes a SQL query for **Analyze Organization Hierarchy** using Common Table Expressions (CTEs), relational JOINs, GROUP BY aggregations. Edge cases: replaces NULL values using `COALESCE` guard.

## Complexity detail
- **Time Complexity**: $O(a + n log n)$ — Operation count bound.
- **Space Complexity**: $O(a + n)$ — Auxiliary memory allocation bound.
