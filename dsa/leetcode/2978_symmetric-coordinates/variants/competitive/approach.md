## General
Executes a SQL query for **Symmetric Coordinates** using Common Table Expressions (CTEs), relational JOINs, window ranking functions, GROUP BY aggregations. Edge cases: filters aggregated group boundaries using `HAVING` clause.

## Complexity detail
- **Time Complexity**: $O(R + D log(D))$ — Operation count bound.
- **Space Complexity**: $O(D)$ — Auxiliary memory allocation bound.
