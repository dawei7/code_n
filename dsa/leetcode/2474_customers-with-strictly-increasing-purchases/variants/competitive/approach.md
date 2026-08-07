## General
Executes a SQL query for **Customers With Strictly Increasing Purchases** using Common Table Expressions (CTEs), relational JOINs, GROUP BY aggregations. Edge cases: replaces NULL values using `COALESCE` guard, filters aggregated group boundaries using `HAVING` clause.

## Complexity detail
- **Time Complexity**: $O(r log r)$ — Operation count bound.
- **Space Complexity**: $O(r)$ — Auxiliary memory allocation bound.
