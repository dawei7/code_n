## General
Given Table: $\text{library}_{books}$, the database query executes a relational pipeline using relational `JOIN` operations to correlate matching records across tables, `GROUP BY` aggregations to summarize record groups. Edge case handling: filters aggregated group results via `HAVING` predicates.

## Complexity detail
- **Time Complexity**: $O(B log B + R log R)$ — Operation count bound.
- **Space Complexity**: $O(B + R)$ — Auxiliary memory allocation bound.
