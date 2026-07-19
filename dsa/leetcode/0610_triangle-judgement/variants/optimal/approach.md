## General
**Apply all three triangle inequalities**

Three positive lengths form a nondegenerate triangle exactly when each pair has a sum strictly greater than the remaining side. Test $x + y > z$, $x + z > y$, and $y + z > x$ in one `CASE` expression.

**Classify rows independently**

When all three comparisons hold, emit `Yes`; otherwise emit `No`. Keep `x`, `y`, and `z` in the projection so each classification remains attached to its original triple.

**Why the predicate is exact**

If one side is at least the sum of the other two, the shorter segments cannot meet to enclose positive area, so `No` is required. Conversely, when every side is shorter than the sum of the other two, the segments can meet and enclose a nondegenerate triangle. The conjunction therefore accepts exactly the valid triples.

## Complexity detail
For `R` rows, the query performs a constant number of arithmetic comparisons per row, giving $O(R)$ time. The returned relation contains `R` rows and therefore occupies $O(R)$ result space; the classification itself needs only constant working state per row.

## Alternatives and edge cases
- **Sort or identify the longest side:** for positive lengths it is sufficient to check that the two shorter sides sum to more than the longest, but sorting each three-value row is less direct in SQL.
- **Use `GREATEST`:** compare twice the greatest side with $x + y + z$; this is concise in MySQL but less portable across local SQL engines.
- **Equality is degenerate:** a row such as `(1, 1, 2)` must be `No` because the inequality is strict.
- The largest value may appear in any of the three columns, so omitting any one inequality is unsafe.
- Equilateral and isosceles triples are valid when the strict inequalities hold.
- Duplicate input rows are classified independently and remain duplicated in the result.
