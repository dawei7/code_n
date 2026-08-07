## General
Given Table: `UserActivity`, the database query executes a relational pipeline using `GROUP BY` aggregations to summarize record groups. Edge case handling: filters aggregated group results via `HAVING` predicates.

## Complexity detail
- **Time Complexity**: $O(A\log A)$ — Operation count bound.
- **Space Complexity**: $O(A)$ — Auxiliary memory allocation bound.
