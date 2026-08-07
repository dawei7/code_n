## General
Executes a SQL query for **Finding the Topic of Each Post** using relational JOINs, GROUP BY aggregations. Edge cases: replaces NULL values using `COALESCE` guard.

## Complexity detail
- **Time Complexity**: $O(pkL + t log t)$ — Operation count bound.
- **Space Complexity**: $O(t)$ — Auxiliary memory allocation bound.
