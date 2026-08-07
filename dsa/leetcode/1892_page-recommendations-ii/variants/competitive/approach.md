## General
Given Table: `Friendship`, the database query executes a relational pipeline using Common Table Expressions (CTEs) to separate intermediate logic into modular subqueries, relational `JOIN` operations to correlate matching records across tables, `GROUP BY` aggregations to summarize record groups.

## Complexity detail
- **Time Complexity**: $O((F+L+C)\log C)$ — Operation count bound.
- **Space Complexity**: $O(F+L+C)$ — Auxiliary memory allocation bound.
