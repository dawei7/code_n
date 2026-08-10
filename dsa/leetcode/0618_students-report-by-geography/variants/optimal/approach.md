## General

**The desired table is a rank-aligned pivot.** Each continent supplies an alphabetically sorted list of names. Row 1 should contain the first name from America, the first from Asia, and the first from Europe; row 2 should contain the second name from each list; and so on. A missing name at a rank becomes `NULL`. SQL rows do not initially contain that cross-continent alignment key, so the query first creates one.

**Assign an independent rank inside every continent.** The CTE computes

`ROW_NUMBER() OVER (PARTITION BY continent ORDER BY name) AS rk`.

`PARTITION BY continent` restarts numbering for America, Asia, and Europe. `ORDER BY name` makes rank 1 the alphabetically smallest name in that continent, rank 2 the next, and so forth. Unlike `RANK` or `DENSE_RANK`, `ROW_NUMBER` always assigns a distinct sequence number to every row.

That distinction is essential because the input may contain duplicate rows. If America contains two students named `Alex`, both occurrences must survive as two positions. `ROW_NUMBER` gives them different ranks even though their names compare equal. Their internal tie order does not matter because the displayed values are identical.

After this step, the sample is conceptually:

| `name` | `continent` | `rk` |
|---|---|---:|
| Jack | America | 1 |
| Jane | America | 2 |
| Xi | Asia | 1 |
| Pascal | Europe | 1 |

**Group equal ranks to form output rows.** `GROUP BY rk` brings the three possible continent entries for a rank into one group. SQL still needs to turn those vertical rows into three horizontal columns. Each output expression conditionally keeps the name for one continent:

- `IF(continent = 'America', name, NULL)` keeps only America's name;
- the Asia and Europe expressions do the same for their continents.

Within one `rk` group, at most one row belongs to a given continent because `ROW_NUMBER` assigned unique ranks inside that partition. The conditional expression is therefore non-null at most once per output column.

**Why `MAX` is used even though nothing is being numerically maximized.** A grouped query must aggregate values that are not part of the grouping key. `MAX` ignores `NULL` values and returns the sole non-null name for the requested continent. If no such row exists at that rank, every input to `MAX` is `NULL`, so the result is `NULL`. This is exactly the desired pivot behavior.

For rank 1 in the sample, the America expression sees `Jack` plus nulls and returns `Jack`; Asia returns `Xi`; Europe returns `Pascal`. For rank 2, only America contributes `Jane`, so the other two aggregates return `NULL`.

**Why all required rows are retained.** The CTE contains every student row. Grouping by rank creates one output group for every rank that appears in any continent. Therefore, the exact window-and-group approach does not actually need America to be the largest partition: if Asia had rank 10 while America ended at rank 8, the `rk = 10` group would still exist and would show `NULL` for America. The statement's largest-America guarantee was more important to older join-based solutions that used America as the driving list.

**Why the values are correct.** Fix a continent `c` and a positive rank `r`. If that continent has at least `r` rows, its alphabetically ordered row number `r` is present in the `rk = r` group. The conditional expression for `c` keeps that row's name and maps every other continent to `NULL`, so `MAX` returns exactly the rank-`r` name. If the continent has fewer than `r` rows, no row in the group passes its condition, so `MAX` returns `NULL`. Applying this reasoning to all three columns and every existing rank proves the pivot contents.

**A final ordering caveat.** `ORDER BY name` inside the window determines which name receives each rank, but it does not order the final grouped rows. SQL does not guarantee result order without a top-level `ORDER BY`. The exact query groups by `rk` and many MySQL executions will happen to emit groups in increasing rank, but that behavior is not a portable guarantee. To guarantee that names appear top-to-bottom alphabetically, the final query should explicitly use `ORDER BY rk`. The pivot values are rank-correct; their presentation order is the material weakness in the literal source.

The quoted aliases `'America'`, `'Asia'`, and `'Europe'` produce the required column labels in MySQL. Identifier quoting with backticks would be clearer, but these simple aliases are accepted in the intended dialect.

## Complexity detail

Let $R$ be the number of rows in `Student`. Computing `ROW_NUMBER` requires arranging rows by `continent` and `name`. A general sort-based implementation costs $O(R\log R)$ time. Once ranks exist, conditional aggregation scans the rows and groups by rank in $O(R)$ expected time with hashing or $O(R\log R)$ with sorting. The manifest's overall $O(R\log R)$ time bound is therefore appropriate.

The ranked CTE, sorting workspace, or grouping table may store $O(R)$ values, matching the manifest's $O(R)$ auxiliary-space bound. Each input row contributes to exactly one rank group and evaluates three constant-size conditional expressions. The number of output rows equals the largest continent count, which is at most $R$.

Adding `ORDER BY rk` to guarantee presentation order does not worsen the stated asymptotic bound: sorting at most $R$ result groups remains $O(R\log R)$, and engines may already have ranks in suitable order.

## Alternatives and edge cases

- **Three ranked CTEs plus joins:** Rank each continent separately, then full-outer-join on rank. This is visually direct but verbose, and MySQL lacks a native full outer join.
- **Session variables:** The editorial's older MySQL technique manually increments one counter per continent. Window functions are clearer, declarative, and less sensitive to evaluation-order behavior.
- **Conditional aggregation with `ROW_NUMBER`:** The exact method is compact and naturally keeps all continents, including when the promised largest partition changes.
- **Explicit final `ORDER BY rk`:** Add this to make alphabetical vertical display guaranteed rather than relying on incidental group output order.
- **Duplicate names:** `ROW_NUMBER` gives each occurrence its own rank, so duplicates are preserved as required.
- **A continent with no students:** Its conditional aggregate is `NULL` at every rank produced by other continents.
- **Only one populated continent:** Every output row contains one name and two `NULL` values.
- **Unequal continent sizes:** Shorter lists correctly become `NULL` after their last rank.
- **Unexpected continent value:** It receives ranks in the CTE and can create groups, but none of the three conditional columns displays its name. The stated domain must remain America, Asia, and Europe.
- **Equal names within one continent:** Their relative row numbers are nondeterministic, but the visible values are identical, so the report is unchanged.
- **Column order:** The three select expressions are deliberately written America, Asia, Europe; changing their order would violate the requested schema even if the values remained correct.
