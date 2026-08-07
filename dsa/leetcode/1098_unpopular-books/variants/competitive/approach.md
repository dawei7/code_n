## General
Executes a SQL query for **Unpopular Books** using relational JOINs, GROUP BY aggregations. Edge cases: replaces NULL values using `COALESCE` guard, filters aggregated group boundaries using `HAVING` clause.

## Complexity detail
- **Time Complexity**: $O((B + O) \log (B + O))$ — Operation count bound.
- **Space Complexity**: $O(B + O)$ — Auxiliary memory allocation bound.
