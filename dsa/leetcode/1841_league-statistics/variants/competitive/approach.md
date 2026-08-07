## General
Given Table: `Teams`, the database query executes a relational pipeline using Common Table Expressions (CTEs) to separate intermediate logic into modular subqueries, relational `JOIN` operations to correlate matching records across tables, `GROUP BY` aggregations to summarize record groups.

## Complexity detail
- **Time Complexity**: $O(m + t\log t)$ — Operation count bound.
- **Space Complexity**: $O(m + t)$ — Auxiliary memory allocation bound.
