## General
### Beginner-Friendly Relational Pipeline Strategy
To Table: `Sales`, this database query builds a step-by-step SQL pipeline.

### Step-by-Step Query Execution
**Step 4: Grouping & Aggregations**  
It groups rows together using `GROUP BY` and calculates sums, averages, or counts for each group.  

### Edge Case Handling & PostgreSQL Standards
- **ANSI SQL Standard:** Follows PostgreSQL standards for cross-platform reliability.


## Complexity detail
- **Time Complexity**: $O(R + Dlog D)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(D)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
