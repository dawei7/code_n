## General
**Group at the requested reporting grain.** Group every row by `query_name`. Duplicate rows remain separate inputs to the aggregates, as required by the table semantics.

**Average the quality contribution directly.** Convert `rating` and `position` to a non-integer numeric ratio before applying `AVG`. This prevents integer division from truncating values such as $5/2$. Round the resulting group average to two decimal places only after aggregation.

**Turn the poor predicate into an indicator.** Map `rating < 3` to 1 and every other rating to 0. Its group average is the fraction of poor rows; multiplying by 100 converts that fraction to a percentage. Rounding after multiplication produces the requested two-decimal result.

Each aggregate sees exactly the rows belonging to its query name, so the two formulas match their definitions independently. A local `ORDER BY query_name` makes fixture output deterministic even though the platform allows any row order.

## Complexity detail
With hash aggregation, the database scans all $n$ rows once and performs constant work per row, for $O(n)$ logical time. It maintains one fixed aggregate record for each of the $g$ query names, using $O(g)$ auxiliary space. A physical engine may choose a sort-based plan with different costs.

## Alternatives and edge cases
- **Correlated aggregate per name:** Recomputing the averages by rescanning `Queries` for every distinct name can take $O(gn)$ time.
- **Redundant cross join:** Repeating every source row once per table row leaves averages unchanged but creates $O(n^2)$ intermediate rows.
- **Integer division:** Dividing two integers may truncate the quality contribution and produce a wrong average.
- **Rating exactly three:** It is not poor because the definition uses strictly less than 3.
- **No poor rows:** Averaging zero indicators produces `0.00` rather than `NULL`.
- **All poor rows:** The poor query percentage is `100.00`.
- **Duplicate rows:** Every occurrence contributes to the numerator and denominator.
- **Rounding order:** Round the final averages, not each individual ratio before averaging.
