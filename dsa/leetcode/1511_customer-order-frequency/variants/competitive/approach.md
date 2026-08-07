## General
Executes a SQL query for **Customer Order Frequency** using relational JOINs, GROUP BY aggregations. Edge cases: filters aggregated group boundaries using `HAVING` clause.

## Complexity detail
- **Time Complexity**: $O(C + P + O\log O)$ — Operation count bound.
- **Space Complexity**: $O(C + P + O)$ — Auxiliary memory allocation bound.
