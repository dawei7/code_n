## General
### Beginner-Friendly Relational Pipeline Strategy
To Table: `Enrollments`, this database query builds a step-by-step SQL pipeline.

### Step-by-Step Query Execution
**Step 1: Common Table Expressions (CTEs)**  
The query uses `WITH` clauses to break complex database transformations into small, easy-to-read virtual tables. This makes the query modular and simple to understand.  
**Step 3: PostgreSQL Window Functions**  
Analytical functions (`ROW_NUMBER()`, `RANK()`, `LAG()`, etc.) calculate relative rankings or running totals within specified partitions without collapsing individual rows.  

### Edge Case Handling & PostgreSQL Standards
- **ANSI SQL Standard:** Follows PostgreSQL standards for cross-platform reliability.


## Complexity detail
- **Time Complexity**: $O(R \log R)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(R)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
