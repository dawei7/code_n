## General
**Competitive Approach — Find Students Who Improved**

The query executes a structured relational pipeline for **Find Students Who Improved**. It uses Common Table Expressions (CTEs) to isolate intermediate data transformations into modular steps, PostgreSQL window functions for analytical ranking and offset calculations, `GROUP BY` aggregation with PostgreSQL standard functions (`COALESCE`, `STRING_AGG`).

**Why This Approach Was Chosen:**
Sourced for PostgreSQL standard compliance. It avoids non-standard vendor extensions (e.g. replacing SQLite `IFNULL` with ANSI `COALESCE` and `GROUP_CONCAT` with `STRING_AGG`), ensuring portable, high-performance database execution.

## Complexity detail
- **Time Complexity**: $O(r log r)$ — Operation count proportional to input scale.
- **Space Complexity**: $O(r)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **PostgreSQL Standards:** Strict alignment with ANSI/PostgreSQL syntax.
- **Readable CTE Design:** Breaks complex multi-stage relational logic into maintainable, self-documenting subqueries.
