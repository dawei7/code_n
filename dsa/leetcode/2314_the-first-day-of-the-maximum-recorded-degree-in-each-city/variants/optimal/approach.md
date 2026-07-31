## General

Each city needs one complete input row, chosen by two priorities: higher `degree` is better, and among equal degrees an earlier `day` is better. This is a top-one-per-group problem where retaining only `MAX(degree)` would lose the associated date and would not resolve ties.

Partition the weather records by `city_id` and assign `ROW_NUMBER()` under `ORDER BY degree DESC, day ASC`. Within a city, position 1 is therefore a maximum-degree row; if several such rows exist, the ascending secondary key guarantees it is the earliest one.

Filter to position 1 and explicitly order the remaining rows by `city_id`. The window rank is not selected, so the result has exactly the requested three columns. Every city contributes exactly one row because every nonempty partition has one first position.

## Complexity detail

Let $r$ be the number of weather records. In the general database execution model, ordering the partitions and the final result takes $O(r\log r)$ time. The ranked intermediate relation and sorting workspace can use $O(r)$ auxiliary space. Available indexes and optimizer strategies may reduce physical sorting work, but the declared bounds do not assume them.

## Alternatives and edge cases

- **Aggregate then join:** Computing each city's maximum degree and joining it back still returns multiple tied dates unless a second aggregation selects the earliest day.
- **Correlated subquery:** Testing every row against its city's maximum and minimum qualifying date is valid, but can repeat work without suitable indexes.
- **Negative degrees:** Descending numeric order still selects the least negative value as the maximum.
- **Repeated maximum:** The earliest date among maximum-degree rows wins; an earlier date with a lower degree does not.
- **Output ordering:** Choosing the correct row per city does not imply result order, so the final ascending `city_id` sort is required.
