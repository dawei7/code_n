## General
Executes a SQL query for **Active Users** using Common Table Expressions (CTEs), relational JOINs, window ranking functions, GROUP BY aggregations. Edge cases: filters aggregated group boundaries using `HAVING` clause.

## Complexity detail
- **Time Complexity**: $O(L\log L+A)$ — Operation count bound.
- **Space Complexity**: $O(L)$ — Auxiliary memory allocation bound.
