## General

**Normalize two outcome tables into one timeline**

The input stores failed dates and succeeded dates in separate tables, but the output needs one chronological sequence of state intervals. The common table expression `T` converts both sources to the same two-column shape:

- `dt` is the task date;
- `st` is the literal state, either `'failed'` or `'succeeded'`.

Each branch filters with `YEAR(...)=2019` before combining the rows. Dates from 2018 or another year therefore cannot influence ranks, groups, or output endpoints.

`UNION ALL` retains every selected row without paying for duplicate elimination. Each source date is a primary key, and the problem states that one task runs per day, so a valid dataset assigns a day one state rather than presenting duplicate same-state rows. Under that contract, deduplication is unnecessary.

**The gaps-and-islands idea**

The desired output is a set of maximal “islands” of consecutive dates with the same state. The central challenge is to create a group key that stays constant while dates are consecutive and changes after a gap.

Within each state, the query assigns dates a rank in increasing order:

`RANK() OVER (PARTITION BY st ORDER BY dt)`.

Partitioning by `st` means failed dates are ranked independently from succeeded dates. Because dates within each source are unique, `RANK` produces consecutive integers \(1,2,3,\ldots\), behaving the same as `ROW_NUMBER` here.

The query subtracts that integer number of days from each date:

`SUBDATE(dt, rank) AS pt`.

Suppose failed dates are January 4 and January 5. Their ranks among failed dates are one and two. Subtracting gives January 3 for both:

\[
\text{Jan 4}-1\text{ day}=\text{Jan 3},
\qquad
\text{Jan 5}-2\text{ days}=\text{Jan 3}.
\]

The shifted date `pt` is constant because both the real date and rank advance by one across consecutive rows.

Now suppose the next failed date is January 9, after successful days create a gap. Its failed-state rank may be three, but January 9 minus three days is January 6, not January 3. The key changes, starting a new failed island.

**Why state must be part of the group**

The derived `pt` alone is not globally unique. A failed island and a succeeded island could coincidentally produce the same shifted date. The outer query therefore groups by both `st` and `pt` using `GROUP BY 1, pt`, where ordinal one refers to the first selected grouping expression, `st`.

Within one such group, every row has the same state and belongs to one consecutive run. `MIN(dt)` is its first date and `MAX(dt)` is its last date. The aliases produce exactly the requested columns:

- `st AS period_state`;
- `MIN(dt) AS start_date`;
- `MAX(dt) AS end_date`.

A one-day island contains one row, so its minimum and maximum are naturally the same date.

**Why the shifted key identifies exactly maximal runs**

Take two adjacent rows in date order within the same state partition. Let their dates, viewed as day numbers, be \(d_1<d_2\), and their consecutive ranks be \(r\) and \(r+1\). Their shifted keys are equal exactly when

\[
d_1-r=d_2-(r+1),
\]

which simplifies to \(d_2-d_1=1\). Thus two successive same-state rows share a key precisely when their calendar dates are consecutive.

By transitivity, every date in a consecutive run shares one key. At the first gap of at least two days, the shifted key changes. Therefore, grouping by state and shifted key neither splits a valid run nor joins two runs separated by another state.

**Following the example**

After the 2019 filters, `T` contains succeeded dates January 1, 2, 3, and 6, plus failed dates January 4 and 5. In the succeeded partition, the first three ranks subtract to the same shifted date, while January 6 has rank four and produces a different key because of the two-date gap within that state. In the failed partition, January 4 and 5 share a key.

Grouping yields three islands: succeeded January 1 through 3, failed January 4 through 5, and succeeded January 6 through 6. The final `ORDER BY 2` uses the second selected output column, `start_date`, so these state intervals appear chronologically.

**SQL-specific details in the exact source**

`SUBDATE(date, integer)` in MySQL interprets the integer as a number of days. That is what makes the rank subtraction work. The query uses ordinal references in `GROUP BY 1` and `ORDER BY 2`. They are concise but depend on select-list position; spelling out `st` and `start_date` would be more explicit without changing the algorithm.

The selected `*` inside the derived table carries `dt`, `st`, and the new `pt` outward. Only the three required aggregates and labels are projected by the final query.

## Complexity detail

Let \(d\) be the total number of 2019 rows from both tables. Filtering and combining rows is linear in the rows examined, subject to database indexing and optimization. The window function must order dates within each state, and the grouping and final ordering may also require sorting or hashing. A conventional upper bound for this plan is \(O(d\log d)\) time.

The intermediate union, window results, and grouping structures can hold \(O(d)\) rows, giving \(O(d)\) working space. Actual database execution plans may use indexes, external sorting, or disk-backed temporary tables, so SQL complexity describes logical growth rather than a guaranteed physical implementation.

## Alternatives and edge cases

- **`LAG` plus cumulative group numbers:** Compare each date with the previous date and state, mark every break, and cumulatively sum break flags. This is explicit and flexible but needs multiple window stages.
- **Recursive calendar generation:** Generate every 2019 date and join outcomes before grouping runs. It can work, but it processes the entire calendar and is more elaborate than ranking existing daily rows.
- **`UNION` instead of `UNION ALL`:** It would perform unnecessary duplicate elimination under the one-task-per-day and primary-key guarantees.
- **`ROW_NUMBER` instead of `RANK`:** The two are equivalent here because each state’s dates are unique. If duplicates were allowed, `RANK` gaps could break the shifted-key property.
- **Dates outside 2019:** They are filtered before ranking, so they cannot shift rank values or extend an interval across the reporting boundary.
- **One-day period:** `MIN(dt)` and `MAX(dt)` return the same date, as required.
- **Alternating outcomes every day:** Each date becomes its own island because consecutive rows of the same state are separated by a calendar gap.
- **One state for all reported days:** All rows share one state and consecutive shifted key, producing one interval.
- **Empty 2019 input:** The CTE has no rows and the query returns no intervals. The stated system model normally supplies one task every day.
- **Dialect dependence:** `YEAR` and integer-form `SUBDATE` are MySQL syntax. Other engines need equivalent date extraction and date arithmetic.
- **Ordinal grouping and ordering:** `GROUP BY 1` means the first selected grouping column and `ORDER BY 2` means `start_date`. Reordering the select list without updating ordinals would change behavior.
