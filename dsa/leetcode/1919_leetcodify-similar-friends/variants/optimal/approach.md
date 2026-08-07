## General
Given Table: `Listens`, the database query executes a relational pipeline using relational `JOIN` operations to correlate matching records across tables, `GROUP BY` aggregations to summarize record groups. Edge case handling: filters aggregated group results via `HAVING` predicates.

## Complexity detail
- **Time Complexity**: $O(L^2 + F)$ — Operation count bound.
- **Space Complexity**: $O(L^2)$ — Auxiliary memory allocation bound.
