## General
Given Table: `Employees`, the database query executes a relational pipeline using relational `JOIN` operations to correlate matching records across tables, `GROUP BY` aggregations to summarize record groups. Edge case handling: replaces `NULL` values using `COALESCE` guards, filters aggregated group results via `HAVING` predicates.

## Complexity detail
- **Time Complexity**: $O((E + L)\log(E + L))$ — Operation count bound.
- **Space Complexity**: $O(E + L)$ — Auxiliary memory allocation bound.
