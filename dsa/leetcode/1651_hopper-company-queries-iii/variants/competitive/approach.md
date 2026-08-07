## General
Given Table: `Drivers`, the database query executes a relational pipeline using Common Table Expressions (CTEs) to separate intermediate logic into modular subqueries, relational `JOIN` operations to correlate matching records across tables, `GROUP BY` aggregations to summarize record groups. Edge case handling: replaces `NULL` values using `COALESCE` guards.

## Complexity detail
- **Time Complexity**: $O(r+a)$ — Operation count bound.
- **Space Complexity**: $O(a)$ — Auxiliary memory allocation bound.
