## General
Executes a SQL query for **Find Emotionally Consistent Users** using Common Table Expressions (CTEs), relational JOINs, GROUP BY aggregations. Edge cases: filters aggregated group boundaries using `HAVING` clause.

## Complexity detail
- **Time Complexity**: $O(R log R + U log U)$ — Operation count bound.
- **Space Complexity**: $O(R + U)$ — Auxiliary memory allocation bound.
