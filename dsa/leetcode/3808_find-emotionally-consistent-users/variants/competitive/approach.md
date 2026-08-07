## General
Given Table: `reactions`, the database query executes a relational pipeline using Common Table Expressions (CTEs) to separate intermediate logic into modular subqueries, window functions for positional ranking and partition analytical operations, `GROUP BY` aggregations to summarize record groups.

## Complexity detail
- **Time Complexity**: $O(R log R + U log U)$ — Operation count bound.
- **Space Complexity**: $O(R + U)$ — Auxiliary memory allocation bound.
