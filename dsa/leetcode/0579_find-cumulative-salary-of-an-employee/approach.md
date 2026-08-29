## General

For every reported employee-month row, the required value is the salary in that calendar month plus the salaries in the two immediately preceding calendar months. Two details make this more subtle than an ordinary running sum:

- missing calendar months contribute zero rather than causing the window to jump to an older recorded row;
- each employee’s most recent recorded month must not appear in the result.

The query handles the first detail with a value-based window frame and the second with a grouped subquery.

**Removing each employee’s latest month**

The subquery

```sql
SELECT id, MAX(month)
FROM Employee
GROUP BY id
```

creates one pair per employee: the employee ID and that employee’s greatest recorded month. The outer `WHERE` excludes rows whose `(id, month)` pair appears in this set:

```sql
WHERE (id, month) NOT IN (...)
```

Using a pair is essential. Month 8 might be the latest month for employee 1 but an ordinary earlier month for a different employee. Comparing only `month` would incorrectly remove rows across employees. The composite comparison ties each maximum to its own ID.

The primary key is `(id, month)`, so these columns are non-`NULL` and unique together. That makes the composite `NOT IN` safe from the confusing unknown result that nullable values can introduce.

An employee with only one salary record has that sole row selected as the maximum and therefore has no output rows. This exactly follows “do not include the most recent month”; there is no other worked month to report.

**Why filtering before the window does not damage earlier sums**

SQL logically applies `WHERE` before window functions. Thus, the most recent row is removed before `SUM(...) OVER (...)` is evaluated. That might initially seem dangerous, but the frame for an earlier month looks only at the current month and prior months. A removed most-recent month is later than every retained month for that employee, so it could never belong to any retained row’s backward-looking frame. Removing it changes only the row that should not be output, not any earlier result.

**Partitioning keeps employees independent**

`PARTITION BY id` starts a separate window calculation for every employee. Salary records belonging to one ID can never enter another employee’s sum. Within each partition, `ORDER BY month` establishes calendar-month order.

The frame is:

```sql
RANGE 2 PRECEDING
```

With the default endpoint of the current row, this means all rows whose ordering value lies from `current month - 2` through `current month`. If the current month is 7, only recorded months 5, 6, and 7 are eligible. Missing rows for 5 or 6 simply contribute nothing, which is equivalent to salaries of zero.

This is why `RANGE` is the right concept. `ROWS 2 PRECEDING` would mean the previous two *records*, regardless of their month numbers. For employee 1 in the sample, the previous recorded months before 7 are 4 and 3, but they are not the previous two calendar months. A row-based frame would incorrectly include those old salaries. The range-based frame sees the gap and returns only month 7’s salary, 90.

Because `(id, month)` is unique, there is at most one salary row for a particular employee-month. The frame does not need to combine duplicate monthly records.

**Tracing one employee**

Employee 1 has recorded months 1, 2, 3, 4, 7, and 8 in the complete conceptual example sequence; the provided rows include the latest month 8, which is filtered from output. For month 4, the numeric window `[2,4]` contains months 2, 3, and 4, so the sum is $30+40+60=130$. For month 3, `[1,3]` gives $20+30+40=90$. For month 2, month 0 is absent and the range contains recorded months 1 and 2, yielding 50. For month 7, `[5,7]` contains only month 7, yielding 90.

The outer `ORDER BY id, month DESC` is separate from the ascending order used inside the window. Window ordering determines which rows contribute to each sum. Final ordering determines display order: IDs ascend, and months within an employee descend. These two orderings can legitimately point in different directions because they have different jobs.

**Why the query is correct**

For each employee, the maximum-month subquery identifies exactly the prohibited latest row, and the composite anti-membership filter removes exactly that row. For any retained row at month $x$, partitioning restricts candidates to the same employee, while `RANGE 2 PRECEDING` restricts them to month values in $[x-2,x]$. Summing `salary` therefore adds exactly the current and previous two calendar months that have records; absent months add nothing, equivalent to zero. No nonworked month becomes an output row because the query begins only from rows in `Employee`.

Finally, the outer sort produces ascending ID and descending month order. Every requested row, value, exclusion, and ordering rule is therefore satisfied.

## Complexity detail

Let $R$ be the number of salary records. Grouping by employee to find maxima takes expected $O(R)$ time with hash aggregation, while a sort-based plan can take $O(R\log R)$. Evaluating the window requires rows to be organized by `id` and `month`. Without a covering order already available, sorting dominates at $O(R\log R)$. The final requested ordering can often reuse or partially reuse ordered data, but the conservative declared time remains $O(R\log R)$.

The maximum-month relation contains at most one row per employee. Window and sort processing can materialize up to $R$ rows, so the declared auxiliary working space is $O(R)$. Database indexes and optimizer choices can reduce sorting or lookup cost, but SQL does not force a specific physical plan.

## Alternatives and edge cases

- **Three self-joins:** Join each current row to the same employee at `month - 1` and `month - 2`, replacing missing salaries with zero. This directly models the three months but is longer and less adaptable than a window.
- **`ROWS 2 PRECEDING`:** This is incorrect when recorded months have gaps because it chooses prior rows rather than prior calendar values.
- **Correlated range subquery:** For every row, sum salaries with matching ID and month between `month - 2` and `month`. It is clear but may repeat range lookups for many rows.
- **`ROW_NUMBER` for latest exclusion:** Rank each employee’s rows by month descending, discard rank one, and then compute sums from an unfiltered base relation. This needs careful query layering so the latest row remains available during any calculation that needs it.
- **Single recorded month:** It is the employee’s most recent month and is entirely excluded.
- **Gaps in employment:** Missing months do not create rows and contribute zero. `RANGE` preserves this calendar meaning.
- **January or February:** Months below 1 have no records, so the range naturally adds only existing months.
- **Different employees with the same latest month:** The composite `(id, month)` comparison excludes each employee’s own maximum without cross-contamination.
- **Window order versus output order:** Ascending month inside `OVER` defines a backward numeric frame; descending month in the final `ORDER BY` only formats results.
- **Null behavior:** Primary-key columns `id` and `month` are non-`NULL`, avoiding the usual `NOT IN` null trap.
- **Only worked months reported:** Since every output originates from an `Employee` row, the query never invents a row for a missing calendar month.
