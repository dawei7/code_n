## General
Given Table: `Products`, the database query executes a relational pipeline using Common Table Expressions (CTEs) to separate intermediate logic into modular subqueries, relational `JOIN` operations to correlate matching records across tables, `GROUP BY` aggregations to summarize record groups.

## Complexity detail
- **Time Complexity**: $O((P+R)\log(P+R))$ — Operation count bound.
- **Space Complexity**: $O(P+R)$ — Auxiliary memory allocation bound.
