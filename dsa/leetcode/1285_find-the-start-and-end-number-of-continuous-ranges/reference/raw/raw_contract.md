## Function Contract

**Input**

- `Logs`: a table containing one row for each unique integer `log_id`.

Let $n$ be the number of input rows and $r$ the number of maximal continuous ranges.

**Output**

Return a table with these columns:

- `start_id`: the smallest identifier in a maximal range.
- `end_id`: the largest identifier in that same range.

Return exactly one row for each of the $r$ ranges, ordered by `start_id` in ascending order. A range containing one identifier has equal start and end values.
