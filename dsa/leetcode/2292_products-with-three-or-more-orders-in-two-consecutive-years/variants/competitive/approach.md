## General
Executes a SQL query for **Products With Three or More Orders in Two Consecutive Years** using Common Table Expressions (CTEs), window ranking functions, GROUP BY aggregations. Edge cases: filters aggregated group boundaries using `HAVING` clause.

## Complexity detail
- **Time Complexity**: $O(r log r)$ — Operation count bound.
- **Space Complexity**: $O(g)$ — Auxiliary memory allocation bound.
