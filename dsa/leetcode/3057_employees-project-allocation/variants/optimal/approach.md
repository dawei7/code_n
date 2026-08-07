## General
### Beginner-Friendly Relational Pipeline Strategy
To Table: `Project`, this database query builds a step-by-step SQL pipeline.

### Step-by-Step Query Execution
**Step 1: Common Table Expressions (CTEs)**  
The query uses `WITH` clauses to break complex database transformations into small, easy-to-read virtual tables. This makes the query modular and simple to understand.  
**Step 2: Relational JOIN Operations**  
It combines matching rows across tables using `INNER JOIN` or `LEFT JOIN` on foreign keys so related information appears in a single record set.  
**Step 4: Grouping & Aggregations**  
It groups rows together using `GROUP BY` and calculates sums, averages, or counts for each group.  

### Edge Case Handling & PostgreSQL Standards
- **ANSI SQL Standard:** Follows PostgreSQL standards for cross-platform reliability.


## Complexity detail
- **Time Complexity**: $O(n log n)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(n)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
