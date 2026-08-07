## General
Executes a SQL query for **Find Users with High Token Usage** using GROUP BY aggregations. Edge cases: filters aggregated group boundaries using `HAVING` clause.

## Complexity detail
- **Time Complexity**: $O(R log R + U log U)$ — Operation count bound.
- **Space Complexity**: $O(R + U)$ — Auxiliary memory allocation bound.
