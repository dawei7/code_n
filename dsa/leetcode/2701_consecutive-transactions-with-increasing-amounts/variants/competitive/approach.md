## General
Executes a SQL query for **Consecutive Transactions with Increasing Amounts** using Common Table Expressions (CTEs), window ranking functions, GROUP BY aggregations. Edge cases: filters aggregated group boundaries using `HAVING` clause.

## Complexity detail
- **Time Complexity**: $O(R log R)$ — Operation count bound.
- **Space Complexity**: $O(R)$ — Auxiliary memory allocation bound.
