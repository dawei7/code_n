## General
Executes a SQL query for **Find Zombie Sessions** using GROUP BY aggregations. Edge cases: filters aggregated group boundaries using `HAVING` clause.

## Complexity detail
- **Time Complexity**: $O(N log N + S log S)$ — Operation count bound.
- **Space Complexity**: $O(N + S)$ — Auxiliary memory allocation bound.
