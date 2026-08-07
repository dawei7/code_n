## General
Given Table: `Users`, the database query executes a relational pipeline using relational `JOIN` operations to correlate matching records across tables, `GROUP BY` aggregations to summarize record groups. Edge case handling: replaces `NULL` values using `COALESCE` guards.

## Complexity detail
- **Time Complexity**: $O((U + R) log (U + R))$ — Operation count bound.
- **Space Complexity**: $O(U + R)$ — Auxiliary memory allocation bound.
