## General
Given Table: `Visits`, the database query executes a relational pipeline using relational `JOIN` operations to correlate matching records across tables. Edge case handling: replaces `NULL` values using `COALESCE` guards.

## Complexity detail
- **Time Complexity**: $O(N\log N)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
