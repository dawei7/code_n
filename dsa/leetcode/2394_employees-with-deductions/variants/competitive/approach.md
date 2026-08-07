## General
Executes a SQL query for **Employees With Deductions** using relational JOINs, GROUP BY aggregations. Edge cases: replaces NULL values using `COALESCE` guard, filters aggregated group boundaries using `HAVING` clause.

## Complexity detail
- **Time Complexity**: $O((E + L)\log(E + L))$ — Operation count bound.
- **Space Complexity**: $O(E + L)$ — Auxiliary memory allocation bound.
