## General
Executes a SQL query for **Biggest Single Number** using GROUP BY aggregations. Edge cases: replaces NULL values using `COALESCE` guard, filters aggregated group boundaries using `HAVING` clause.

## Complexity detail
- **Time Complexity**: $O(R \log R)$ — Operation count bound.
- **Space Complexity**: $O(R)$ — Auxiliary memory allocation bound.
