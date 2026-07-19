## General
**Reduce the multiset to single values**

Group rows by `num` and retain only groups whose `COUNT(*)` equals one. Each surviving group represents exactly one value that occurs once in the complete table.

**Select the greatest survivor**

Apply an outer `MAX(num)` to the filtered groups. Since every eligible value appears once in that derived relation, the maximum is precisely the greatest single number.

**Preserve the empty-result contract**

An aggregate without `GROUP BY` always emits one row. Therefore, when the filtered relation is empty, `MAX` yields null rather than omitting the result row. This distinguishes the required answer from simply sorting the filtered groups and taking a row.

## Complexity detail
For `R` rows, grouping distinct values takes $O(R \log R)$ time in the comparison-based database model and $O(R)$ execution space in the worst case where every value is distinct. The outer maximum scans at most `R` groups and does not increase those bounds.

## Alternatives and edge cases
- **Window frequency:** attach `COUNT(*) OVER (PARTITION BY num)` to each row, filter frequency one, and take `MAX`; it has the same asymptotic bound and retains row-level data longer.
- **Correlated frequency count:** count matching rows separately for every input row; it is correct but can take $O(R^2)$ time.
- **Order and limit:** sorting single groups descending with `LIMIT 1` returns no row when no single exists unless another outer aggregate or null-producing wrapper is added.
- Negative values are compared normally; the greatest may still be negative.
- Zero is a valid single number.
- A value appearing two or more times is excluded regardless of how large it is.
- When exactly one row exists, its value is the answer.
