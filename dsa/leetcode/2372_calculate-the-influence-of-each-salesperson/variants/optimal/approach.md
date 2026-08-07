## General
Executes a SQL query for **Calculate the Influence of Each Salesperson** using relational JOINs, GROUP BY aggregations. Edge cases: replaces NULL values using `COALESCE` guard.

## Complexity detail
- **Time Complexity**: $O((S+C+R) log(S+C+R))$ — Operation count bound.
- **Space Complexity**: $O(S+C+R)$ — Auxiliary memory allocation bound.
