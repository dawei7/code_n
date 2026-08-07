## General
Given Table: `Seat`, the database query executes a relational pipeline using relational `JOIN` operations to correlate matching records across tables. Edge case handling: replaces `NULL` values using `COALESCE` guards.

## Complexity detail
- **Time Complexity**: $O(R \log R)$ — Operation count bound.
- **Space Complexity**: $O(R)$ — Auxiliary memory allocation bound.
