## General

**Define one complete priority order inside each city**

For every city, the desired row is selected by two rules in sequence:

1. Prefer a larger `degree`.
2. If several rows have that same maximum degree, prefer the earlier `day`.

These rules can be encoded directly as an ordering. Descending degree puts the hottest records first, and ascending day puts the earliest record first among equal degrees. Once every city's rows have that order, the answer is simply its first row.

The common table expression `T` computes a window rank using

`PARTITION BY city_id ORDER BY degree DESC, day`.

Partitioning is essential. It restarts the ranking independently for each city, so a very hot measurement in one city has no effect on which row is selected for another city.

**Why the two order directions are different**

`degree DESC` places a higher numerical degree before a lower one. This also works when all recorded values are negative. For example, `-6` is greater than `-7` and therefore appears first under descending numeric order.

The next key `day` uses SQL's default ascending direction. It matters only after degrees tie because it appears second in the ordering list. Earlier dates sort before later dates, implementing the required tie-break.

Changing either direction changes the problem. Ascending degree would choose the coldest record, while descending day would choose the latest occurrence of a city's maximum rather than the first.

**Why `RANK() = 1` leaves exactly one row per city**

The window function assigns rank one to the first ordering key combination within each city. In general, `RANK` can assign the same rank to tied rows. Here a complete tie would require both the same `degree` and the same `day` within one city.

The table's primary key is `(city_id, day)`. A city cannot have two rows on the same day, so two rows in the same partition cannot tie on the `day` key. Even when several rows share the maximum degree, their dates are different and the earlier date orders first. Therefore exactly one row per city receives `rk = 1`.

The outer `WHERE rk = 1` keeps that unique winning row and removes every later record. Using `RANK` is safe because the order is total inside each valid city partition; `ROW_NUMBER` would produce the same winner.

**Return only the source columns in globally requested order**

The CTE uses `SELECT *` and adds `rk`, so it temporarily carries all three Weather columns plus the helper rank. The outer query projects `city_id, day, degree`, exactly the requested output schema, and does not expose `rk`.

Finally, `ORDER BY 1` sorts by the first expression in the select list, which is `city_id`. SQL's default direction is ascending, so this satisfies the required global city order.

The final ordering serves a different purpose from the ordering inside the window. The window order selects the best row within each city; it does not guarantee the order in which different city partitions are returned. The outer `ORDER BY` is therefore necessary even after correct ranking.

**A direct trace through a tie**

Suppose city 2 has degrees 37 on August 7 and August 17. Both rows tie on the first key `degree DESC`. The second key compares their dates in ascending order, so August 7 precedes August 17 and receives rank one. `WHERE rk = 1` keeps August 7.

Suppose city 3 has `-7` in February and `-6` in December. Since `-6 > -7`, descending degree places December first despite its later date. The date tie-break is not consulted because the degrees differ. This demonstrates the correct priority: date never outweighs a larger temperature.

**Why the query is complete and correct**

Fix any city. Its rows are sorted by the exact lexicographic priority pair `(-degree, day)`: negating the degree is a conceptual way to express descending degree while keeping day ascending. The first row has no smaller priority pair. Therefore no row has a greater degree; if another row has the same degree, none has an earlier day.

That first row is precisely the city's maximum recorded degree at its earliest occurrence. Primary-key uniqueness makes it the sole rank-one row. Partitioning repeats the same argument independently for every city, filtering keeps all and only those winners, and the final sort arranges them by ascending `city_id`. Every requirement is thus handled by a distinct clause of the query.

## Complexity detail

Let `r` be the number of rows in `Weather`. Evaluating the window order may require sorting rows by city and by the within-city keys, which takes `O(r \log r)` time with a general comparison sort. The final output ordering by `city_id` can also require sorting, but another `O(r \log r)` operation does not change the overall bound. A database optimizer may exploit an index or preserve a useful intermediate order, but the logical worst-case analysis remains `O(r \log r)`.

Window evaluation and sorting may buffer or materialize `O(r)` rows, yielding `O(r)` working space. MySQL may keep those rows in memory or spill them to temporary storage depending on execution settings. The query returns one row per distinct city, which is at most `r`; output storage is normally excluded from auxiliary-space accounting.

The comparisons of integer degrees and fixed-format date values are treated as constant time. No self-join or correlated subquery causes repeated full scans per city.

## Alternatives and edge cases

- **`ROW_NUMBER` with the same ordering:** This is equally correct and explicitly guarantees one row per partition. Under the unique `(city_id, day)` key, it selects the same row as `RANK`.
- **Aggregate maximum degree then join:** Compute `MAX(degree)` per city, join matching rows, and aggregate `MIN(day)` among the ties. This is valid but requires multiple logical stages and careful grouping to return the matching degree.
- **Correlated subqueries:** For each row, test whether a higher degree or an equal degree with an earlier day exists. This can be correct but is more verbose and may be less efficient without suitable indexes.
- **Use `MAX(day)` with `MAX(degree)` in one grouping:** Independent maxima may come from different source rows, producing a date that did not record the maximum degree. The tie-break must be applied only among maximum-degree rows.
- **Order by day before degree:** That would select the earliest weather record in the city, even when a later day is hotter. Degree has higher priority.
- **Order degree ascending:** This selects the minimum recorded degree and is incorrect, especially easy to overlook with negative values.
- **Order day descending:** This selects the latest occurrence of the maximum rather than the required earliest occurrence.
- **Several maximum-degree days:** The ascending date key makes exactly the earliest one rank first.
- **All degrees negative:** Numeric descending order still selects the greatest value, such as `-2` over `-10`. No special sign handling is needed.
- **One row for a city:** It is automatically rank one and is returned.
- **Many cities with the same maximum degree:** Partitions are independent, so cross-city ties never interact.
- **Duplicate day within a city:** The primary key forbids it. Without that guarantee, complete ordering ties could give more than one row `rk = 1`.
- **No final `ORDER BY`:** SQL does not promise partition or CTE output order. Correct row selection alone would not satisfy the requested ascending city presentation.
- **`ORDER BY 1` readability:** It correctly refers to `city_id` because that is the first projected column. Writing `ORDER BY city_id` would be more explicit but would not change the result.
- **Helper rank column:** It exists only inside `T` and is intentionally omitted from the final projection.
