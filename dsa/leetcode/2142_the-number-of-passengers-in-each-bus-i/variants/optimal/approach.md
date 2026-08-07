## General
### Beginner-Friendly Relational Pipeline Strategy
To Table: `Buses`, this database query builds a step-by-step SQL pipeline.

### Step-by-Step Query Execution
**Step 2: Relational JOIN Operations**  
It combines matching rows across tables using `INNER JOIN` or `LEFT JOIN` on foreign keys so related information appears in a single record set.  
**Step 3: PostgreSQL Window Functions**  
Analytical functions (`ROW_NUMBER()`, `RANK()`, `LAG()`, etc.) calculate relative rankings or running totals within specified partitions without collapsing individual rows.  
**Step 4: Grouping & Aggregations**  
It groups rows together using `GROUP BY` and calculates sums, averages, or counts for each group.  

### Edge Case Handling & PostgreSQL Standards
- **ANSI SQL Standard:** Follows PostgreSQL standards for cross-platform reliability.


## Complexity detail
- **Time Complexity**: $O(N log N)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(N)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
