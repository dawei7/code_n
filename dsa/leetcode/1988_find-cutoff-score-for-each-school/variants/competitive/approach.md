## General
Given Table: `Schools`, the database query executes a relational pipeline using relational `JOIN` operations to correlate matching records across tables, `GROUP BY` aggregations to summarize record groups. Edge case handling: replaces `NULL` values using `COALESCE` guards.

## Complexity detail
- **Time Complexity**: $O(SE)$ — Operation count bound.
- **Space Complexity**: $O(S)$ — Auxiliary memory allocation bound.
