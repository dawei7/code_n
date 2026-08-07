## General
Executes a SQL query for **Customer Who Visited but Did Not Make Any Transactions** using relational JOINs, GROUP BY aggregations (`COALESCE`, `STRING_AGG`).

## Complexity detail
- **Time Complexity**: $O((V+T)\log(V+T))$ — Operation count bound.
- **Space Complexity**: $O(V+T)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Algorithm design:** Describes the specific algorithmic approach used in the solution.
- **Complexity bounds:** Declares the precise time and space complexity guarantees.
