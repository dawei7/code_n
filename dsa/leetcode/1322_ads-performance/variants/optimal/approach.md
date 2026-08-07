## General
Executes a SQL query for **Ads Performance** using GROUP BY aggregations. Edge cases: replaces NULL values using `COALESCE` guard.

## Complexity detail
- **Time Complexity**: $O(r+a\log a)$ — Operation count bound.
- **Space Complexity**: $O(a)$ — Auxiliary memory allocation bound.
