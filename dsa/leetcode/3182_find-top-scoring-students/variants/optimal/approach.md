## General
Given Table: `students`, the database query executes a relational pipeline using relational `JOIN` operations to correlate matching records across tables, `GROUP BY` aggregations to summarize record groups. Edge case handling: filters aggregated group results via `HAVING` predicates.

## Complexity detail
- **Time Complexity**: $O(r log r)$ — Operation count bound.
- **Space Complexity**: $O(r)$ — Auxiliary memory allocation bound.
