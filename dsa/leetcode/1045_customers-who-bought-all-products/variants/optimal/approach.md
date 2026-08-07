## General
Given Table: `Customer`, the database query executes a relational pipeline using `GROUP BY` aggregations to summarize record groups. Edge case handling: filters aggregated group results via `HAVING` predicates.

## Complexity detail
- **Time Complexity**: $O(R log R + Q)$ — Operation count bound.
- **Space Complexity**: $O(R+Q)$ — Auxiliary memory allocation bound.
