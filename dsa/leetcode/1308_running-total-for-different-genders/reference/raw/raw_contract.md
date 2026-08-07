## Function Contract

**Input**

- `Scores`: the score table described above.

Let $n$ be the number of score rows.

**Return value**

Return a table with these columns:

- `gender`: the team identifier from the input row.
- `day`: the date from the input row.
- `total`: the sum of `score_points` for that gender on every recorded date up to and including `day`.

Return one output row for every input row. Sort first by `gender` in ascending order and then by `day` in ascending order.
