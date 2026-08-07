## General
Given Table: $\text{customer}_{transactions}$, the database query executes a relational pipeline using `GROUP BY` aggregations to summarize record groups. Edge case handling: filters aggregated group results via `HAVING` predicates.

## Complexity detail
- **Time Complexity**: $O(N log N + C log C)$ — Operation count bound.
- **Space Complexity**: $O(N + C)$ — Auxiliary memory allocation bound.
