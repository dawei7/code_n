## General
Given Table: `drivers`, the database query executes a relational pipeline using Common Table Expressions (CTEs) to separate intermediate logic into modular subqueries, relational `JOIN` operations to correlate matching records across tables, `GROUP BY` aggregations to summarize record groups.

## Complexity detail
- **Time Complexity**: $O(T log T + D log D)$ — Operation count bound.
- **Space Complexity**: $O(T + D)$ — Auxiliary memory allocation bound.
