## General
Given Table: `ProductPurchases`, the database query executes a relational pipeline using relational `JOIN` operations to correlate matching records across tables, `GROUP BY` aggregations to summarize record groups. Edge case handling: filters aggregated group results via `HAVING` predicates.

## Complexity detail
- **Time Complexity**: $O(P\log P + J\log J + I\log I)$ — Operation count bound.
- **Space Complexity**: $O(J + I)$ — Auxiliary memory allocation bound.
