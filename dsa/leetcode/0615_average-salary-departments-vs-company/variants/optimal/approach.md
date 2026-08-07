## General
**Optimal Approach — Average Salary: Departments VS Company**

The query executes a structured relational pipeline for **Average Salary: Departments VS Company**. It uses Common Table Expressions (CTEs) to isolate intermediate data transformations into modular steps, Relational JOIN operations to correlate records across tables.

**Why This Approach Was Chosen:**
Sourced for PostgreSQL standard compliance. It avoids non-standard vendor extensions (e.g. replacing SQLite `IFNULL` with ANSI `COALESCE` and `GROUP_CONCAT` with `STRING_AGG`), ensuring portable, high-performance database execution.

## Complexity detail
- **Time Complexity**: $O((S + E) \log(S + E))$ — Operation count proportional to input scale.
- **Space Complexity**: $O(S + E)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **PostgreSQL Standards:** Strict alignment with ANSI/PostgreSQL syntax.
- **Readable CTE Design:** Breaks complex multi-stage relational logic into maintainable, self-documenting subqueries.
