## General
Given Table: `Listens`, the database query executes a relational pipeline using Common Table Expressions (CTEs) to separate intermediate logic into modular subqueries, relational `JOIN` operations to correlate matching records across tables. Edge case handling: filters aggregated group results via `HAVING` predicates.

## Complexity detail
- **Time Complexity**: $O(L^2 + F)$ — Operation count bound.
- **Space Complexity**: $O(L^2)$ — Auxiliary memory allocation bound.
