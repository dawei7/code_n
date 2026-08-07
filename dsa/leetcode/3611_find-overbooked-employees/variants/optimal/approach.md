## General
Given Table: `employees`, the database query executes a relational pipeline using Common Table Expressions (CTEs) to separate intermediate logic into modular subqueries, relational `JOIN` operations to correlate matching records across tables, `GROUP BY` aggregations to summarize record groups.

## Complexity detail
- **Time Complexity**: $O(M log M + E log E)$ — Operation count bound.
- **Space Complexity**: $O(M + E)$ — Auxiliary memory allocation bound.
