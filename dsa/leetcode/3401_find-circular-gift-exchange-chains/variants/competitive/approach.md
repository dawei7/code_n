## General
Given Table: `SecretSanta`, the database query executes a relational pipeline using Common Table Expressions (CTEs) to separate intermediate logic into modular subqueries, relational `JOIN` operations to correlate matching records across tables, window functions for positional ranking and partition analytical operations, `GROUP BY` aggregations to summarize record groups.

## Complexity detail
- **Time Complexity**: $O(e^2)$ — Operation count bound.
- **Space Complexity**: $O(e^2)$ — Auxiliary memory allocation bound.
