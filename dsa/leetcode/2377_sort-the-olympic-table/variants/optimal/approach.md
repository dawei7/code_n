## General

The output contains every input row unchanged; only row order changes. SQL's `ORDER BY` can express the ranking rules directly and in their stated priority order.

**Apply medal keys from strongest to weakest.** Sort `gold_medals`, `silver_medals`, and `bronze_medals` in descending order. SQL consults each later key only when all earlier keys tie, matching the medal hierarchy exactly.

**Finish with the opposite direction for names.** When all three medal counts tie, sort `country` ascending. Because `country` is the primary key, this final key also makes the complete ordering deterministic.

Selecting the four requested columns and applying those four keys preserves all rows. For any pair of countries, the first key on which they differ determines their order according to the contract, so the result is the required Olympic table.

## Complexity detail

Let $R$ be the number of rows. A general comparison sort takes $O(R\log R)$ time and $O(R)$ working space. A database index matching the requested ordering may allow a more direct ordered scan, but the portable query does not assume one.

## Alternatives and edge cases

- **Window ranking:** Computing `ROW_NUMBER` with the same four ordering keys and then sorting by that rank is equivalent but redundant.
- **Pairwise rank subquery:** Counting how many countries outrank each row can reproduce the order but may take $O(R^2)$ comparisons.
- **Gold priority:** Any gold advantage wins regardless of silver or bronze counts.
- **Silver and bronze ties:** Each lower medal is consulted only after all higher medals tie.
- **Country direction:** The name tie-breaker is ascending, unlike the three medal columns.
- **Zero medals:** Zero-count countries remain in the table and follow the same ordering rules.
