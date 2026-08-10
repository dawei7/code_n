## General

Each input row records points for one gender on one date. The required `total` is not an independent aggregate that collapses the whole gender into one row. It is a running total: every original row must remain, and its value must include points for that gender from the earliest recorded date through the current row's date.

A window function is designed for this combination of detail and aggregation. It computes a value over a related set of rows while preserving one output row per input row.

**Separating the two teams**

The expression begins with

`SUM(score_points) OVER (PARTITION BY gender ...)`.

`PARTITION BY gender` creates an independent window partition for each distinct gender. Female rows contribute only to female totals, and male rows contribute only to male totals. The running accumulation restarts when the partition changes.

This partitioning is different from `GROUP BY gender`. A grouped query would reduce each gender to one row, losing the per-day results. The window aggregate keeps the original `gender` and `day` row while attaching a cumulative sum.

**Putting dates in accumulation order**

Inside each partition, `ORDER BY gender, day` determines the order used by the window calculation. Because every row in a partition already has the same `gender`, the first ordering key is redundant there. `ORDER BY day` would define the same within-gender sequence.

For one gender, the earliest date comes first. Its window includes its own score, so its total equals that first score. The next date includes both the first and second rows, and so on.

For example, female scores $17$, $23$, $17$, and $23$ in ascending date order produce totals $17$, $40$, $57$, and $80$. The value $57$ is not the score for one day; it is $17+23+17$ through that date.

**The implicit window frame**

MySQL supplies a default frame when an aggregate window has `ORDER BY` and no explicit frame clause. Conceptually, the cumulative frame extends from the beginning of the partition through the current ordering value.

The schema declares `(gender, day)` as a primary key, so no gender has two rows on the same day. As a result, peer-row differences between a `RANGE` frame and a `ROWS` frame do not affect this dataset: within a gender, each day identifies one row.

An explicit form such as

`ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`

would make the running-row intent clearer. Under the key guarantee, it produces the same totals as the exact source.

**Why every computed total is correct**

Fix an input row with gender $g$ and date $d$. Partitioning excludes all rows whose gender is not $g$. Window ordering puts rows for $g$ in ascending date order. The cumulative frame contains exactly those partition rows whose date is at or before $d$, including the current row.

`SUM(score_points)` adds precisely those scores. Therefore, the derived `total` matches the requested running total for that gender and day.

The select list preserves `gender` and `day` and adds the alias `total`. Because window functions do not collapse rows, every input row yields one result row.

**The missing final result ordering**

The task also explicitly requires the returned table to be sorted first by `gender` and then by `day`, both ascending. The exact query has an `ORDER BY` only inside `OVER (...)`.

Window ordering controls which rows participate before the current row and in what sequence the running calculation is defined. It does not guarantee the presentation order of the final result set. SQL engines are free to emit rows in another order unless the outer query itself has an `ORDER BY`.

Therefore, the exact source computes the correct cumulative values but does not fully guarantee the required result ordering. A compliant query needs a final clause:

`ORDER BY gender, day`.

This distinction is important because a particular MySQL execution plan may happen to reuse its window sort and display the expected order. That observed order is incidental, not part of the SQL contract. Correct SQL should not depend on it.

**Why no player grouping is needed**

`player_name` is not selected or partitioned. The running total is for the entire gender team, so scores by different players of the same gender belong in the same partition. The primary key promises only one score row per gender and date, even if player names repeat on different dates.

The query also does not need a self-join or correlated subquery. The window frame supplies all prior team rows directly.

## Complexity detail

Let $n$ be the number of rows in `Scores`. A typical execution plan must arrange rows by the partition and ordering keys `(gender, day)`. Without a supporting access order, sorting costs $O(n\log n)$ time. After ordering, the database can maintain a running sum in one pass, costing $O(n)$ additional time.

The window operator or sort may use $O(n)$ working space, matching the manifest's $O(n)$ bound. The final result also contains $n$ rows.

The composite primary key `(gender, day)` may provide an index whose order already matches the needed partition sequence. If the optimizer scans that index, it may avoid an explicit sort and approach $O(n)$ processing time. SQL complexity depends on indexes and the physical plan, so $O(n\log n)$ is a conservative general bound.

Adding the missing outer `ORDER BY gender, day` may reuse the same order in a favorable plan, but SQL does not promise reuse. In the worst case, presentation ordering is still within $O(n\log n)$.

## Alternatives and edge cases

- **Correlated subquery:** For each row, sum same-gender scores with dates at or before the current date. It is logically direct but can approach $O(n^2)$ without effective indexing or optimizer rewriting.
- **Self-join and group:** Joining each row to all earlier same-gender rows and grouping by the current row also works, but creates a large intermediate relation.
- **Explicit `ROWS` frame:** Adding `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` makes cumulative semantics explicit and avoids peer-group surprises if uniqueness changes.
- **Required outer ordering:** The exact source needs final `ORDER BY gender, day`. Window-local order alone is not a result-order guarantee.
- **Redundant gender window key:** Inside a `gender` partition, ordering by `gender` adds no distinction. Keeping it is harmless but less concise than ordering by `day` alone.
- **First date for a gender:** Its frame contains only itself, so total equals that row's score.
- **Only one row for a gender:** That row remains in the output and its total equals its score.
- **Different genders on nearby dates:** Partitioning prevents one team's scores from entering the other team's total.
- **Unique date within gender:** The composite primary key ensures no tied `day` peers in one partition, so implicit `RANGE` and explicit cumulative `ROWS` agree.
- **Negative score outside the likely scenario:** `SUM` would still compute an arithmetic running total, which could decrease. The algorithm does not require monotone scores.
- **No guaranteed natural order:** Table storage and index choice do not replace an outer `ORDER BY` when ordering is part of the answer contract.
