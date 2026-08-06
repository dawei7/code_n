## Description

The `Wineries` table contains uniquely identified point awards associated with
a country and winery. A winery's score is the sum of all its `points` rows
within its country.

For each country, rank wineries by total points descending; when totals tie,
rank the winery whose name is alphabetically smaller first. Return one row per
country with strings `"name (total)"` for ranks one, two, and three under
`top_winery`, `second_winery`, and `third_winery`. If rank two is absent, use
`"No second winery"`; if rank three is absent, use `"No third winery"`.
Order countries ascending.
