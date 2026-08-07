## General
Given Table: $\text{library}_{books}$, the database query executes a relational pipeline using Common Table Expressions (CTEs) to separate intermediate logic into modular subqueries, relational `JOIN` operations to correlate matching records across tables, `GROUP BY` aggregations to summarize record groups.

## Complexity detail
- **Time Complexity**: $O(B log B + R log R)$ — Operation count bound.
- **Space Complexity**: $O(B + R)$ — Auxiliary memory allocation bound.
