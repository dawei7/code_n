## General

**Round each work session before summing**

The company counts session duration in whole minutes, rounding each individual session upward. This order matters:

$$
\sum \left\lceil\frac{\text{session seconds}}{60}\right\rceil
$$

is not always equal to rounding the total seconds once. Two sessions of one minute and one second each count as two minutes each, for four total, whereas their combined two minutes and two seconds would round to three.

The CTE `T` performs the required per-session ceiling inside `SUM`.

**Compute one session's rounded minutes**

`TIMESTAMPDIFF(second, in_time, out_time)` returns the elapsed whole seconds between the two datetimes. It naturally handles a session crossing midnight because both values contain dates, not only clock times.

Dividing by `60` converts seconds to minutes, possibly fractional. `CEILING(...)` raises any partial minute to the next integer. A duration exactly divisible by sixty remains unchanged.

The expression inside the CTE is:

```sql
SUM(CEILING(TIMESTAMPDIFF(second, in_time, out_time) / 60))
```

Grouping by `employee_id` adds all independently rounded session minutes for that employee.

**Convert total minutes to hours**

The CTE divides the summed minutes by `60` and names the result `tot`. This yields total worked hours, possibly fractional, so it can be compared directly with integer `needed_hours`.

Equivalently, the query could keep total minutes and compare against `needed_hours * 60`. The current units are consistent because both sides of:

```sql
tot < needed_hours
```

are hours.

The comparison is strict. An employee who works exactly the required number of hours should not be deducted; only a smaller total qualifies.

**Preserve employees with no logs**

CTE `T` contains only employees who have at least one `Logs` row. The final query begins with `Employees` and performs:

```sql
LEFT JOIN T USING (employee_id)
```

This preserves every employee. For someone with no sessions, `tot` is null. `COALESCE(tot, 0)` converts it to zero before comparison, so an employee needing positive hours is correctly reported.

An inner join would silently drop no-log employees, even though they are precisely people who should receive deductions.

**Trace the sample durations**

Employee one has sessions of exactly eight hours, eight hours four minutes minus one second details that round to the stated minute total, and four hours plus one second. Each session is converted to seconds, divided, and individually rounded upward. Their total exceeds twenty required hours, so the employee is filtered out.

Employee two's session lasts just under twelve hours. Rounded to whole minutes, it is eleven hours fifty-nine minutes, still below twelve, so the employee passes the `WHERE` condition and is returned.

Employee three has no row in `T`. The left join produces null `tot`, `COALESCE` makes it zero, and zero is below two needed hours.

**Why the query is correct**

For each logged employee, the CTE maps every session to exactly the credited minute count specified by the rule, sums those credits, and converts the result to hours. Grouping isolates one employee's sessions from every other employee.

The left join associates each employee with that exact total when present and with null otherwise. Converting absence to zero produces the correct worked time for an employee with no sessions. Finally, the strict less-than filter selects exactly employees whose credited hours do not reach their requirement.

The output asks only for IDs, so no total or required-hours column is selected. Row order may be arbitrary, and the query adds no unnecessary `ORDER BY`.

**Why crossing midnight requires no special branch**

For a session beginning October 12 at 23:00 and ending October 13 after 03:00, `TIMESTAMPDIFF` subtracts full datetimes and obtains a positive duration across the date boundary. Subtracting only time-of-day components would incorrectly look negative; the chosen function avoids that.

## Complexity detail

Let $E$ be the number of employees and $L$ the number of log rows. The manifest gives $O((E+L)\log(E+L))$ time and $O(E+L)$ space for a general sort/group/join execution.

The CTE scans logs and groups by employee. A database may sort or hash for aggregation, then use an indexed, merge, or hash join to employees. Sorting-based plans fit the stated bound; suitable indexes or hashing may approach expected linear time.

Grouping state, join structures, and possible materialized CTE rows use at most linear working space. The result contains no more than $E$ employee IDs.

## Alternatives and edge cases

- **Round after summing seconds:** This is incorrect because the specification rounds every session independently.
- **Compare in minutes:** Keep the summed rounded minutes and test against `needed_hours * 60`. It is equivalent and avoids fractional-hour representation.
- **Inner join:** It loses employees with no sessions, who must be treated as working zero hours.
- **Exact-minute session:** `CEILING` leaves its integer minute count unchanged.
- **Any positive leftover seconds:** The session receives one additional credited minute.
- **Session crossing midnight:** Full datetime difference handles it correctly.
- **Exactly enough total time:** The strict `<` comparison does not report that employee.
- **No logs:** `COALESCE` supplies zero and the employee is deducted because required hours are positive.
- **Multiple sessions:** Each ceiling occurs before `SUM`, preserving the rule.
- **Any output order:** No sorting is required.
