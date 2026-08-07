## General
Given Table: `Candidates`, the database query executes a relational pipeline using Common Table Expressions (CTEs) to separate intermediate logic into modular subqueries. Edge case handling: replaces `NULL` values using `COALESCE` guards.

## Complexity detail
- **Time Complexity**: $O(R\log R)$ — Operation count bound.
- **Space Complexity**: $O(R)$ — Auxiliary memory allocation bound.
