## General
Executes a SQL query for **Product's Worth Over Invoices** using relational JOINs, GROUP BY aggregations. Edge cases: replaces NULL values using `COALESCE` guard.

## Complexity detail
- **Time Complexity**: $O(I + P \log P)$ — Operation count bound.
- **Space Complexity**: $O(P)$ — Auxiliary memory allocation bound.
