## General
Given Table: `Users`, the database query executes a relational pipeline using relational `JOIN` operations to correlate matching records across tables, `GROUP BY` aggregations to summarize record groups. Edge case handling: filters aggregated group results via `HAVING` predicates.

## Complexity detail
- **Time Complexity**: $O((U+T)\log(U+T))$ — Operation count bound.
- **Space Complexity**: $O(U+T)$ — Auxiliary memory allocation bound.
