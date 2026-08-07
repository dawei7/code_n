## General
Executes a SQL query for **Most Common Course Pairs** using Common Table Expressions (CTEs), relational JOINs, window ranking functions, GROUP BY aggregations. Edge cases: filters aggregated group boundaries using `HAVING` clause.

## Complexity detail
- **Time Complexity**: $O(R log R + P log P)$ — Operation count bound.
- **Space Complexity**: $O(R + P)$ — Auxiliary memory allocation bound.
