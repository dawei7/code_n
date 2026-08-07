## General
Given Table: `Products`, the database query executes a relational pipeline using relational `JOIN` operations to correlate matching records across tables. Edge case handling: replaces `NULL` values using `COALESCE` guards.

## Complexity detail
- **Time Complexity**: $O((P + D) log(P + D))$ — Operation count bound.
- **Space Complexity**: $O(P + D)$ — Auxiliary memory allocation bound.
