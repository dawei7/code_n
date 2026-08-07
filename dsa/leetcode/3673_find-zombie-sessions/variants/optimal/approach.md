## General
Given Table: $\text{app}_{events}$, the database query executes a relational pipeline using `GROUP BY` aggregations to summarize record groups. Edge case handling: filters aggregated group results via `HAVING` predicates.

## Complexity detail
- **Time Complexity**: $O(N log N + S log S)$ — Operation count bound.
- **Space Complexity**: $O(N + S)$ — Auxiliary memory allocation bound.
