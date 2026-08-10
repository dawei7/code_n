## General

**Convert three long-format columns into a two-dimensional lookup.** Each input row describes one observation:

`(city, month) -> temperature`.

In long format, city and month repeat across rows. The requested wide format uses each distinct month as a row key, each distinct city as a column key, and places the corresponding temperature at their intersection.

The exact solution states those three roles directly:

`weather.pivot(index='month', columns='city', values='temperature')`.

**The `index` argument defines output rows.** Every distinct value from input `month` becomes one label on the returned DataFrame's row index. The word `month` is also retained as the name of that index axis. It may look like a normal first column in a rendered table, but internally it is the row index produced by the pivot.

All input rows for January therefore contribute to the January output row, all February observations to February, and so forth.

**The `columns` argument defines output columns.** Every distinct city name becomes a column label. In the example, `ElPaso` and `Jacksonville` are no longer values repeated down a `city` column. They become headers identifying two temperature Series in the wide result.

**The `values` argument supplies cells.** For each input record, pandas reads its month $m$, city $c$, and temperature $t$, then places $t$ into output coordinate $(m,c)$. The source does not aggregate or transform temperatures. A value `13` for Jacksonville in January remains `13` at row January and column Jacksonville.

**Why `pivot` requires unique coordinate pairs.** A single DataFrame cell cannot hold two independent temperature values. Therefore, if the input has multiple rows with the same month and city, plain `pivot` raises an error rather than guessing how to combine them. The task's intended data supplies one temperature per pair. When duplicates require aggregation, `pivot_table` with an explicit function such as mean or maximum is the appropriate different operation.
Take any valid input row $(c,m,t)$. By the definitions of the three arguments, the returned table has row label $m$, column label $c$, and stores $t$ at their intersection. Uniqueness ensures no other row competes for that cell. Conversely, every populated output cell arises from an input row with exactly its month and city labels. Thus the reshape preserves every temperature fact while representing the two categorical dimensions as axes.

For example, input rows `(ElPaso, April, 2)` and `(Jacksonville, April, 5)` share output row April. Their different city labels place `2` and `5` in separate columns. No arithmetic combines them.

**What happens to missing combinations.** In a general incomplete grid, suppose a month has no observation for one city. The wide output still has that month row and city column because each exists elsewhere, and their intersection receives a missing value. The example supplies a complete city-month grid, so every displayed cell is filled.

**Ordering is library behavior, not the core mapping.** pandas may order the unique index and column labels according to its pivot or unstack implementation and dtype. The example displays alphabetically ordered months rather than calendar order. The exact source does not add a calendar-category conversion or explicit reindexing. If calendar order were a separate requirement, it would need an ordered categorical or a specified month list after pivoting.

**The input remains long format.** `pivot` returns a reshaped DataFrame; the source does not assign into `weather` or request in-place behavior. The original three-column table remains semantically unchanged.

**Why this is not a group-by problem.** Grouping and aggregating are useful when many observations share a key. Here the required transformation is one-to-one: each unique key pair already identifies one value. `pivot` communicates that stronger uniqueness expectation and avoids inventing an aggregation rule.

## Complexity detail

Let $r$ be the number of input observations, $m$ the number of distinct months, and $c$ the number of distinct cities. pandas must process the $r$ keys and organize them for reshaping; the manifest models this as $O(r\log r)$ key ordering plus $O(cm)$ output construction, for total $O(r\log r+cm)$ time.

The wide result contains $cm$ potential cells and therefore needs $O(cm)$ output space. pandas also uses indexes, codes, and temporary reshaping state associated with the $r$ input rows; exact peak memory is implementation-dependent, so a fully explicit accounting can include $O(r+cm)$. The manifest emphasizes the dominant wide-output grid as $O(cm)$.

## Alternatives and edge cases

- **`pivot_table`:** Use it only when duplicate month-city pairs require an explicit aggregation; plain `pivot` correctly rejects ambiguity.
- **Group then unstack:** `groupby` or `set_index(...).unstack()` can reproduce the reshape but is more verbose for unique keys.
- **Duplicate key pair:** The exact source raises instead of choosing one temperature.
- **Missing month-city combination:** The wide cell becomes missing.
- **One city:** The result has one city column and one row per distinct month.
- **One month:** The result has one row and one column per distinct city.
- **Month order:** The source does not enforce chronological order; add categorical ordering only if explicitly required.
- **Index versus ordinary column:** `month` becomes the named row index, which renders like the leftmost table field but is not a regular data column.
