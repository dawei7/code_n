## General
Executes a SQL query for **Find Stores with Inventory Imbalance** using Common Table Expressions (CTEs), relational JOINs, GROUP BY aggregations. Edge cases: filters aggregated group boundaries using `HAVING` clause.

## Complexity detail
- **Time Complexity**: $O(R log R + S log S)$ — Operation count bound.
- **Space Complexity**: $O(R + S)$ — Auxiliary memory allocation bound.
