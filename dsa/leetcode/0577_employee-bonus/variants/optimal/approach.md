## General
Given Table: `Employee`, the database query executes a relational pipeline using relational `JOIN` operations to correlate matching records across tables. Edge case handling: replaces `NULL` values using `COALESCE` guards.

## Complexity detail
- **Time Complexity**: $O((E + B) \log(E + B))$ — Operation count bound.
- **Space Complexity**: $O(E + B)$ — Auxiliary memory allocation bound.
