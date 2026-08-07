## General
Executes a SQL query for **Employees With Deductions** using Common Table Expressions (CTEs), relational JOINs, GROUP BY aggregations. Edge cases: replaces NULL values using `COALESCE` guard.

## Complexity detail
- **Time Complexity**: $O((E + L)\log(E + L))$ — Operation count bound.
- **Space Complexity**: $O(E + L)$ — Auxiliary memory allocation bound.
