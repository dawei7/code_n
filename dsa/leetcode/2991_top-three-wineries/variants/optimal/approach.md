## General

**Aggregate before ranking.** Group by `(country, winery)` and sum `points` so
multiple awards for one winery become one total. Ranking raw rows would split
a winery's score and violate the contract.

**Create a deterministic order per country.** Apply `ROW_NUMBER` partitioned
by country, ordering totals descending and winery names ascending. Because the
name resolves equal totals, ranks one through three identify exactly the
requested wineries.

**Pivot ranks into one country row.** Conditional aggregates place each of the
first three formatted `name (total)` strings into its output column.
`COALESCE` supplies the exact second- and third-place messages when those ranks
do not exist. Grouping the ranked rows by country and sorting countries
ascending completes the result. Each stage mirrors one contract operation, so
every output cell has the required winery or its mandated fallback.

## Complexity detail

Let $R$ be the number of point rows. Aggregation and partition ordering take
$O(R\log R)$ time in the general comparison-based model. Grouped and window
state can occupy $O(R)$ space.

## Alternatives and edge cases

- **Correlated rank count:** Counting better wineries for every aggregate is correct but can take quadratic time.
- **Rank raw rows:** This is wrong when one winery has multiple point records; totals must be combined first.
- **Equal totals:** Winery name ascending is a required tie-breaker, so tied scores still receive distinct positions.
- **One winery:** Both `No second winery` and `No third winery` are required.
- **Two wineries:** Only the third-place placeholder is used.
- **More than three:** Lower-ranked wineries do not appear in any output column.
