## General
Given Table: `Purchases`, the database query executes a relational pipeline using Common Table Expressions (CTEs) to separate intermediate logic into modular subqueries, relational `JOIN` operations to correlate matching records across tables, `GROUP BY` aggregations to summarize record groups. Edge case handling: replaces `NULL` values using `COALESCE` guards.

## Complexity detail
- **Time Complexity**: $O(R log R)$ — Operation count bound.
- **Space Complexity**: $O(R)$ — Auxiliary memory allocation bound.
