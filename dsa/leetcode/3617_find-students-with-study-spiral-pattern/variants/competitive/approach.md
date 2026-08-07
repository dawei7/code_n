## General
Given Table: `students`, the database query executes a relational pipeline using Common Table Expressions (CTEs) to separate intermediate logic into modular subqueries, relational `JOIN` operations to correlate matching records across tables, window functions for positional ranking and partition analytical operations, `GROUP BY` aggregations to summarize record groups. Edge case handling: filters aggregated group results via `HAVING` predicates.

## Complexity detail
- **Time Complexity**: $O(R log R + S log S)$ — Operation count bound.
- **Space Complexity**: $O(R + S)$ — Auxiliary memory allocation bound.
