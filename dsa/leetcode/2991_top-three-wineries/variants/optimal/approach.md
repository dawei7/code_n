## General

**Rank wineries only after combining their rows**

A winery may appear in several rows. Its ranking score is its total points, not the largest single row and not the number of appearances. The innermost query groups by `country` and `winery` and calculates `SUM(points) AS points`.

After this stage, each country/winery pair has exactly one row. For example, RoyalVines has rows worth 47 and 39 points in the sample, so its grouped total is 86 before any ranking occurs.

Grouping by both columns is necessary because the same winery name in different countries would represent separate country rankings.

**Rank within each country with the required tie-breaker**

CTE `T` applies:

`RANK() OVER (PARTITION BY country ORDER BY points DESC, winery) AS rk`.

`PARTITION BY country` restarts the ranking for every country. Descending points put the largest total first. When totals tie, ascending `winery` name determines their order.

Because the grouped relation has one row per winery name, the two ordering keys together distinguish rows within a country. Thus ranks progress as one, two, three, and so on even though the function used is `RANK`. The winery-name tie-break removes point ties before rank assignment.

The same CTE formats each candidate as:

`CONCAT(winery, ' (', points, ')')`.

This produces strings such as `"HarmonyHill (100)"`, already in the exact output form.

**Pivot ranks into one country row**

The desired output has separate columns for the top, second, and third wineries. The query treats `T AS t1` as the rank-one row by applying `WHERE t1.rk = 1`.

It left joins `T AS t2` on the same country and `t1.rk = t2.rk - 1`. Since `t1.rk` is one, this seeks rank two. It then left joins `T AS t3` through `t2` with the analogous condition, seeking rank three.

Left joins are crucial. An inner join would remove countries having fewer than three wineries. With left joins, missing rank-two or rank-three rows become `NULL` while the top winery remains.

`COALESCE` converts those nulls to the required text:

- `'No second winery'`;
- `'No third winery'`.

The top winery needs no fallback because every country present in the grouped table has at least one winery and therefore a rank-one row.

**Why the join chain works**

The tie-break makes ranks consecutive. Consequently, if a second winery exists it has rank two, and if a third exists it has rank three. The join arithmetic selects exactly those rows.

If there is no second winery, `t2` is null and the subsequent join through `t2.country` also produces no `t3` row. Both fallback messages appear. If there is a second but no third, only the third fallback appears.

For Australia, grouped totals sort as HarmonyHill 100, GrapesGalore 85, and WhisperingPines 84. They become ranks one, two, and three and are pivoted into the three columns. For Hungary’s single winery, only `t1` exists.


Aggregation yields the exact total points for every winery. The window ordering is exactly the required comparison: greater total first, then lexicographically smaller name. Therefore ranks one through three identify the correct top three.

The joins place those exact ranks into their named columns. Left-join nulls occur exactly when the corresponding rank does not exist, and `COALESCE` supplies the required message. Every country contributes its unique rank-one row, so the output has one row per country.

Finally, `ORDER BY 1` sorts the first selected column, `country`, ascending.

**Formatting happens after numeric ranking**

Ranking uses numeric `points` from the grouped table, not the formatted string. This matters because lexicographic ordering of strings like `"(100)"` and `"(99)"` would not reliably express numeric score order. `CONCAT` is used only for output after the correct ranking keys are established.

## Complexity detail

Let $R$ be the input-row count and $W$ the number of distinct country/winery pairs. Aggregating is $O(R)$ expected with hashing or $O(R\log R)$ with sorting. Window ranking sorts the $W$ totals by country, points, and name, costing $O(W\log W)$ in a general plan.

The three references to `T` can be joined by country/rank using indexes, hashing, or materialized CTE access. Final country sorting is $O(C\log C)$ for $C$ countries. Since $C\le W\le R$, $O(R\log R)$ is a safe overall bound. Intermediate grouped/ranked data uses $O(R)$ worst-case space.

## Alternatives and edge cases

- **Rank raw rows:** This would treat repeated winery entries separately instead of summing their points first.
- **Use `LIMIT 3` globally:** It would return three wineries across all countries, not three per country.
- **Omit winery-name tie-break:** Equal totals would have ambiguous order and `RANK` could assign the same rank, breaking the pivot joins.
- **Conditional aggregation pivot:** `MAX(CASE WHEN rk=1 THEN ... END)` is an equivalent and often simpler pivot; the exact source uses self-joins.
- **Only one winery:** The top value is shown and both fallback messages appear.
- **Exactly two wineries:** Rank two fills `second_winery` and rank three falls back.
- **Repeated winery rows:** `SUM(points)` combines them before ranking.
- **Equal total points:** Ascending winery name establishes a unique order.
- **Output formatting:** Points are summed numerically before being embedded in `"name (points)"`.
- **Country ordering:** `ORDER BY 1` sorts countries ascending.
