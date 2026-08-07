## General
Given Table: `Inventory`, the database query executes a relational pipeline using Common Table Expressions (CTEs) to separate intermediate logic into modular subqueries, relational `JOIN` operations to correlate matching records across tables. Edge case handling: replaces `NULL` values using `COALESCE` guards.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
