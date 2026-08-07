## General
Given Table: `Salesperson`, the database query executes a relational pipeline using relational `JOIN` operations to correlate matching records across tables, `GROUP BY` aggregations to summarize record groups. Edge case handling: replaces `NULL` values using `COALESCE` guards.

## Complexity detail
- **Time Complexity**: $O((S+C+R) log(S+C+R))$ — Operation count bound.
- **Space Complexity**: $O(S+C+R)$ — Auxiliary memory allocation bound.
