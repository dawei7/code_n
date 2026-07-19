## General
**Express the threshold without division**

The required comparison is

$$
\frac{\text{likes}}{\text{likes}+\text{dislikes}} < \frac{3}{5}.
$$

Because vote totals are positive, cross multiplication preserves the
inequality. Test `5 * likes < 3 * (likes + dislikes)`. The strict `<` operator
correctly excludes exactly 60%, and integer arithmetic avoids rounding near
the boundary.

**Filter first, then impose the required order**

Select only `problem_id` from rows satisfying that inequality and sort the
result by `problem_id` ascending. Each row is evaluated independently, so it
is returned exactly when its like proportion meets the definition; the final
ordering clause establishes the required output sequence.

## Complexity detail
Scanning and filtering $P$ rows takes $O(P)$ time. Without relying on a useful
index, sorting as many as $P$ qualifying identifiers takes
$O(P\log P)$ time and $O(P)$ working space. A database may exploit the primary
key order and use less sorting work, but the stated bounds cover the general
plan.

## Alternatives and edge cases
- **Decimal division:** Comparing a computed ratio with `0.6` is readable but
  can introduce type-dependent rounding or integer-division mistakes.
- **Correlated rank ordering:** Sorting by counting how many IDs precede each
  row is correct but repeatedly scans the table and can take $O(P^2)$ time.
- The threshold is strict; exactly 60% is not low quality.
- Input row order does not determine output order.
- A qualifying set may be empty, but the result still has the
  `problem_id` column.
