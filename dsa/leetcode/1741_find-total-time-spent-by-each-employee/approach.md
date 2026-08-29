## General

**Identify what one input row contributes**

Each row of `Employees` records one uninterrupted visit to the office. The visit begins at `in_time` and ends at `out_time`, measured as minute positions within the same `event_day`. Because `in_time < out_time`, the duration contributed by that row is exactly:

$$
\texttt{out\_time}-\texttt{in\_time}.
$$

The task is not asking for one result per visit. It asks for one result per employee per day, and an employee may have several visits on the same day. Therefore the durations of rows that share both `emp_id` and `event_day` must be added together.

The exact SQL solution expresses this in a single aggregation query:

`SUM(out_time - in_time)` calculates and accumulates the row durations, while `GROUP BY 1, 2` partitions rows according to the first two expressions in the `SELECT` list.

**Understand the output columns before grouping**

The first selected expression is `event_day AS day`. The stored date is preserved, but the result column receives the required name `day`. The second selected expression is `emp_id`. The third is the aggregate `SUM(out_time - in_time) AS total_time`.

SQL ordinal grouping makes `GROUP BY 1, 2` refer to those first and second selected expressions. In this query, that means grouping by `event_day` and `emp_id`. It does not mean grouping by literal numeric values one and two, and it does not include `total_time` in the key.

Using both key columns is essential. Grouping only by employee would incorrectly combine visits from different days. Grouping only by day would combine different employees. The pair `(event_day, emp_id)` describes exactly one requested output group.

**How aggregation processes a group**

Conceptually, the database begins with an empty accumulator for every distinct employee-day pair. For each input row, it computes the duration and adds it to the accumulator associated with that row's pair.

For employee one on 2020-11-28 in the example, the two row contributions are:

- `32 - 4 = 28` minutes.
- `200 - 55 = 145` minutes.

Both rows have the same day and employee identifier, so `SUM` combines them into `28 + 145 = 173`. The visit on 2020-12-03 belongs to a different key and therefore produces a separate total of 41. Rows belonging to employee two use different keys even when the day matches employee one's day.

The guarantee that visits do not overlap is useful domain information, but the query does not need interval merging. The requested definition explicitly says that the time for each entry is `out_time - in_time`, and non-overlap guarantees that summing these durations does not double-count office time.

**Why subtraction belongs inside SUM**

`SUM(out_time - in_time)` evaluates the subtraction for each row and then adds the results. By linearity, it could also be written as `SUM(out_time) - SUM(in_time)` for the same non-null numeric data, but keeping the row formula inside `SUM` mirrors the problem definition directly and is easier to audit.

No `WHERE` clause is needed because every input row represents a valid event that should contribute. No join is needed because all grouping keys and duration endpoints are already present in `Employees`. No `ORDER BY` is needed because the result may be returned in any order.

**Why the primary key does not replace GROUP BY**

The table's primary key is `(emp_id, event_day, in_time)`. It prevents two rows from having the same employee, day, and entry minute, but it intentionally permits multiple entry times for one employee on one day. As a result, `(emp_id, event_day)` alone is not unique in the input. Aggregation is precisely what collapses those multiple valid visits into one output row.

Notice that `in_time` must not be part of the grouping key. Including it would keep visits separate and prevent the required daily total. Similarly, `out_time` is a measurement used in the aggregate, not a grouping dimension.

**Why every output row is correct**

Fix any employee identifier $e$ and day $d$. `GROUP BY 1, 2` places in one group exactly the rows whose `event_day` is $d$ and whose `emp_id` is $e$. It places no row for another employee or day in that group.

For every row in the group, `out_time - in_time` equals that visit's duration by the contract. `SUM` adds every such duration once. Therefore `total_time` is exactly the total number of minutes that employee spent in the office on that day. Every input row belongs to exactly one employee-day group, so the query produces one correct result row for every pair present in the data and no spurious pair.

## Complexity detail

Let $R$ be the number of input rows and $G$ the number of distinct `(event_day, emp_id)` groups. Conceptually, the database reads each row, computes one constant-time subtraction, and updates one group accumulator. With hash aggregation, this is expected $O(R)$ time and $O(G)$ working space, matching the manifest.

A database engine is free to choose a sort-based aggregation instead. Such a physical plan can take $O(R\log R)$ time for sorting, particularly when no useful index or hash plan is selected. SQL describes the result rather than forcing a particular execution algorithm, so the manifest states the standard logical or hash-aggregation bound.

The result itself has $G$ rows. Counting returned data, $O(G)$ output space is unavoidable. Each group stores a two-column key and one running sum. The arithmetic per input row and the number of selected expressions are constant.

## Alternatives and edge cases

- **Explicit grouping names:** `GROUP BY event_day, emp_id` is equivalent here and can be safer during query maintenance because reordering the `SELECT` list cannot silently change its meaning.
- **Window function:** `SUM(...) OVER (PARTITION BY ...)` would repeat a daily total on every visit row unless followed by deduplication, so ordinary grouping is simpler.
- **Correlated subquery:** Recomputing the sum for each employee-day pair is more verbose and may repeatedly scan the same rows.
- **Application-side aggregation:** Fetching all visits and grouping them in application code moves work and data transfer out of the database without improving the result.
- **Several visits on one day:** All durations for the same employee-day key are added into one row.
- **Same day, different employees:** `emp_id` keeps their totals separate.
- **Same employee, different days:** `event_day` keeps their totals separate.
- **Single visit:** Its group total is simply `out_time - in_time`.
- **No overlapping events:** Direct summation is valid; interval union or overlap correction is unnecessary.
- **Boundary minute values:** Values from 1 through 1440 are ordinary integers, and the strict endpoint order keeps every duration positive.
- **Output order:** Omitting `ORDER BY` is intentional because any row order is accepted.
- **Alias requirement:** `event_day AS day` supplies the requested result-column name without changing the stored date values.
- **Ordinal syntax:** `GROUP BY 1, 2` is concise but depends on MySQL's interpretation of select-list positions.
- **Primary key semantics:** Different `in_time` values allow multiple rows in one employee-day group, which is why aggregation remains necessary.
