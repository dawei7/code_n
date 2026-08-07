## General
Executes a SQL query for **Sellers With No Sales** using relational JOINs, GROUP BY aggregations. Edge cases: replaces NULL values using `COALESCE` guard, filters aggregated group boundaries using `HAVING` clause.

## Complexity detail
- **Time Complexity**: $O((s+r)\log(s+r))$ — Operation count bound.
- **Space Complexity**: $O(s+r)$ — Auxiliary memory allocation bound.
