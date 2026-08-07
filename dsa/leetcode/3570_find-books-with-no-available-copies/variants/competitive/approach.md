## General
Executes a SQL query for **Find Books with No Available Copies** using relational JOINs, GROUP BY aggregations. Edge cases: filters aggregated group boundaries using `HAVING` clause.

## Complexity detail
- **Time Complexity**: $O(B log B + R log R)$ — Operation count bound.
- **Space Complexity**: $O(B + R)$ — Auxiliary memory allocation bound.
