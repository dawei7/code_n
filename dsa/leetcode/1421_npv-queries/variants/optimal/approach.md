## General
Given Table: `NPV`, the database query executes a relational pipeline using relational `JOIN` operations to correlate matching records across tables. Edge case handling: replaces `NULL` values using `COALESCE` guards.

## Complexity detail
- **Time Complexity**: $O(P+Q)$ — Operation count bound.
- **Space Complexity**: $O(P+Q)$ — Auxiliary memory allocation bound.
