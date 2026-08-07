## General
**Competitive Approach — Friends With No Mutual Friends**

The query executes a structured relational pipeline for **Friends With No Mutual Friends**. It uses Common Table Expressions (CTEs) to isolate intermediate data transformations into modular steps, Relational JOIN operations to correlate records across tables.

**Why This Approach Was Chosen:**
Sourced for PostgreSQL standard compliance. It avoids non-standard vendor extensions (e.g. replacing SQLite `IFNULL` with ANSI `COALESCE` and `GROUP_CONCAT` with `STRING_AGG`), ensuring portable, high-performance database execution.

## Complexity detail
- **Time Complexity**: $O(m d + m log m)$ — Operation count proportional to input scale.
- **Space Complexity**: $O(m)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **PostgreSQL Standards:** Strict alignment with ANSI/PostgreSQL syntax.
- **Readable CTE Design:** Breaks complex multi-stage relational logic into maintainable, self-documenting subqueries.
