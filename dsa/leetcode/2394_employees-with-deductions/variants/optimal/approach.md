## General
Given Table: `Employees`, the database query executes a relational pipeline using Common Table Expressions (CTEs) to separate intermediate logic into modular subqueries, relational `JOIN` operations to correlate matching records across tables, `GROUP BY` aggregations to summarize record groups. Edge case handling: replaces `NULL` values using `COALESCE` guards.

## Complexity detail
- **Time Complexity**: $O((E + L)\log(E + L))$ — Operation count bound.
- **Space Complexity**: $O(E + L)$ — Auxiliary memory allocation bound.
