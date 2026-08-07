## General
Given Table: `sales`, the database query executes a relational pipeline using Common Table Expressions (CTEs) to separate intermediate logic into modular subqueries, relational `JOIN` operations to correlate matching records across tables, window functions for positional ranking and partition analytical operations, `GROUP BY` aggregations to summarize record groups.

## Complexity detail
- **Time Complexity**: $O(S log S + P log P + G log G)$ — Operation count bound.
- **Space Complexity**: $O(S + P + G)$ — Auxiliary memory allocation bound.
