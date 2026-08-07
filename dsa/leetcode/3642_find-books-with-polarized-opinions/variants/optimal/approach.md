## General
Given Table: `books`, the database query executes a relational pipeline using relational `JOIN` operations to correlate matching records across tables, `GROUP BY` aggregations to summarize record groups. Edge case handling: filters aggregated group results via `HAVING` predicates.

## Complexity detail
- **Time Complexity**: $O(R + B log B)$ — Operation count bound.
- **Space Complexity**: $O(B)$ — Auxiliary memory allocation bound.
