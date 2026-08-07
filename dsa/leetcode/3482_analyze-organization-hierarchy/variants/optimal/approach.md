## General
Given Table: `Employees`, the database query executes a relational pipeline using Common Table Expressions (CTEs) to separate intermediate logic into modular subqueries, relational `JOIN` operations to correlate matching records across tables, `GROUP BY` aggregations to summarize record groups. Edge case handling: replaces `NULL` values using `COALESCE` guards.

## Complexity detail
- **Time Complexity**: $O(a + n log n)$ — Operation count bound.
- **Space Complexity**: $O(a + n)$ — Auxiliary memory allocation bound.
