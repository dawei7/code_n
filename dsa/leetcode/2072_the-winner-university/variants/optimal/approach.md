## General
**Aggregate each university independently**

For each table, count only rows whose `score` is at least $90$. A conditional expression inside `COUNT` returns a non-null value for excellent students and null otherwise, producing one scalar count for each university.

**Map the count comparison to the required label**

Cross join the two one-row aggregates and evaluate a `CASE`: choose New York's label when its count is greater, California's when its count is greater, and `No Winner` otherwise. Since each subquery always returns exactly one aggregate row, the result also has exactly one row.

The two conditional counts are precisely the numbers of excellent students because the threshold is inclusive. The three mutually exclusive comparisons—greater, less, and equal—cover every possible relationship, so the selected label exactly matches the competition rule.

## Complexity detail
Each $N$-row table is scanned once, giving $O(N)$ time because the participant counts are equal. Only two scalar aggregates are retained, so the logical auxiliary space is $O(1)$; physical database execution details may vary.

## Alternatives and edge cases
- **Sum Boolean predicates:** In dialects where comparisons are numeric, `SUM(score >= 90)` is concise but less portable than conditional counting.
- **Redundant self-cross-products:** Counting distinct excellent students after joining each table to itself is correct but can materialize $O(N^2)$ row pairs.
- A score of exactly $90$ is excellent.
- The winner depends on excellent-student counts, not total or average scores.
- Equal nonzero counts and equal zero counts both produce `No Winner`.
- Student identifiers are local to their tables and need not be joined across universities.
