## General
Given Table: `UserActivity`, the database query executes a relational pipeline using Common Table Expressions (CTEs) to separate intermediate logic into modular subqueries, relational `JOIN` operations to correlate matching records across tables, `GROUP BY` aggregations to summarize record groups.

## Complexity detail
- **Time Complexity**: $O(A\log A)$ — Operation count bound.
- **Space Complexity**: $O(U)$ — Auxiliary memory allocation bound.
