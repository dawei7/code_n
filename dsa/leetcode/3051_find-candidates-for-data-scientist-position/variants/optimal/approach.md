## General
Given Table: `Candidates`, the database query executes a relational pipeline using `GROUP BY` aggregations to summarize record groups. Edge case handling: filters aggregated group results via `HAVING` predicates.

## Complexity detail
- **Time Complexity**: $O(n + c log c)$ — Operation count bound.
- **Space Complexity**: $O(c)$ — Auxiliary memory allocation bound.
