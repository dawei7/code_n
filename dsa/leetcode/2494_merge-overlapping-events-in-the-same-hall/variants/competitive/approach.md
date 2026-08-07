## General
Executes a SQL query for **Merge Overlapping Events in the Same Hall** using Common Table Expressions (CTEs), GROUP BY aggregations. Edge cases: replaces NULL values using `COALESCE` guard.

## Complexity detail
- **Time Complexity**: $O(r log r)$ — Operation count bound.
- **Space Complexity**: $O(r)$ — Auxiliary memory allocation bound.
