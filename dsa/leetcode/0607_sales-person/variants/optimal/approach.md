## General
Executes a SQL query for **Sales Person** using relational JOINs, GROUP BY aggregations. Edge cases: replaces NULL values using `COALESCE` guard, filters aggregated group boundaries using `HAVING` clause.

## Complexity detail
- **Time Complexity**: $O((S + C + O) \log(S + C + O))$ — Operation count bound.
- **Space Complexity**: $O(S + C + O)$ — Auxiliary memory allocation bound.
