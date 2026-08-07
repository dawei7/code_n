## General
Given Table: `Ads`, the database query executes a relational pipeline using `GROUP BY` aggregations to summarize record groups. Edge case handling: replaces `NULL` values using `COALESCE` guards.

## Complexity detail
- **Time Complexity**: $O(r+a\log a)$ — Operation count bound.
- **Space Complexity**: $O(a)$ — Auxiliary memory allocation bound.
