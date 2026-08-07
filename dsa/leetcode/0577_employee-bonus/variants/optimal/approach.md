## General
Executes a SQL query for **Employee Bonus** using relational JOINs. Edge cases: replaces NULL values using `COALESCE` guard.

## Complexity detail
- **Time Complexity**: $O((E + B) \log(E + B))$ — Operation count bound.
- **Space Complexity**: $O(E + B)$ — Auxiliary memory allocation bound.
