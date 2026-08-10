## General

**Identify the two averages that must be compared.** Every salary payment belongs to an employee, and every employee belongs to one department. For each reporting period and department, the output needs:

1. the average of all company salary amounts in that period, and
2. the average of salary amounts for only that department in the same period.

The exact query computes both values on every joined salary row with window functions. It then keeps one distinct output row per repeated comparison.

**Attach a department before calculating departmental statistics.** `Salary` does not contain `department_id`, so the query first joins `Salary AS s` to `Employee AS e` on their shared `employee_id`. The foreign-key contract means every salary employee has a matching employee row, and the primary key in `Employee` means the join attaches exactly one department rather than duplicating a payment.

**Format the displayed period.** `DATE_FORMAT(pay_date, '%Y-%m')` turns a date such as `2017-03-31` into the requested string `2017-03`. This expression is named `pay_month` and is eventually projected to the result.

**Use windows so both granularities remain available.** A normal `GROUP BY` collapses rows. A window aggregate instead computes a group statistic while leaving every original joined row present.

- `AVG(amount) OVER (PARTITION BY pay_date)` places the company average for an exact payment date on every payment from that date.
- `AVG(amount) OVER (PARTITION BY pay_date, department_id)` places the department average for that exact payment date on every payment for that department and date.

For the three March sample payments, the first window gives all rows the company average `(9000 + 6000 + 10000) / 3`. The department window gives department 1 the average `9000` and both department-2 rows the average `(6000 + 10000) / 2`.

The CTE `t` therefore still has one row per salary payment, but each row now knows its formatted month, department, company average, and department average.

**Translate numerical order into the required labels.** The outer `CASE` follows a complete three-way comparison:

- equal averages produce `'same'`;
- a smaller company average means the department average is larger, so the label is `'higher'`;
- the remaining case means the department average is smaller, so the label is `'lower'`.

The direction of the second condition deserves attention. It reads `company_avg_amount < department_avg_amount`; the requested label describes the department relative to the company, so `'higher'` is correct.

**Why `DISTINCT` is necessary.** Window functions do not reduce row count. If a department has twenty salary rows on a date, all twenty carry the same four derived values. The outer query selects only `pay_month`, `department_id`, and the label, then `DISTINCT` collapses those repeated copies to one result row.

**The exact-date versus calendar-month subtlety.** The displayed key is a calendar month, but both windows partition by the full `pay_date`. Those are equivalent only when all payments that belong to one reporting month use the same exact date. Under that payroll model, each window partition is exactly one month, and the reasoning above proves the result.

The written table contract does not explicitly say that every payment in a calendar month has an identical day. If March payments could occur on both `2017-03-15` and `2017-03-31`, the exact query would compute two separate company and department averages, format both as `2017-03`, and possibly emit multiple labels for the same department-month. Therefore, the exact implementation's correctness proof depends on a same-pay-date-per-month data property. A fully calendar-month-based query should partition by `DATE_FORMAT(pay_date, '%Y-%m')` itself.

**Why the method is correct under its required payroll-date property.** Fix one month `m` and one department `d` having salary rows. The join attaches the correct department to every amount. Because all rows for `m` share one `pay_date`, the first window contains every company amount in `m`, so it computes the company mean. Adding `department_id` to the second partition selects exactly the amounts belonging to `d`, so it computes the department mean. The `CASE` returns the unique correct ordering label between those means, and `DISTINCT` removes repeated copies without changing the label. Thus exactly one correct row remains for `(m, d)`.

## Complexity detail

Let $S$ be the number of salary rows and $E$ the number of employee rows. The key join can be implemented with an index or hash lookup. Window functions generally require partitioning and often sorting the joined salary rows by their partition keys. `DISTINCT` may require another hash set or sort. A conservative database-independent bound is therefore $O((S+E)\log(S+E))$ time, matching the manifest.

The joined working relation, window state, and distinct operation may collectively need $O(S+E)$ auxiliary space. Some engines spill large sorts to disk, but that changes the storage medium rather than the asymptotic amount of working data. The final result contains at most one row per represented department-period under the same-date property.

Computing `AVG` does not require materializing every value once a partition is available: an engine can maintain a sum and count. The sorting or hashing needed to establish partitions dominates that constant aggregate state. Formatting the date and evaluating the `CASE` are constant work per row.

## Alternatives and edge cases

- **Partition by formatted month:** Replace both uses of `pay_date` in the window partitions with `DATE_FORMAT(pay_date, '%Y-%m')`. This preserves the convenient window design and correctly combines payments made on different days of the same month.
- **Two grouped CTEs:** Compute one company average per month and one department average per month, then join them on `pay_month`. This mirrors the editorial, produces already-collapsed rows, and removes the need for outer `DISTINCT`.
- **Conditional comparison without floating rounding:** Compare the database's `AVG` results directly, as the source does. Manually rounding averages before comparing can turn genuinely different values into `'same'`.
- **One department in a month:** Its average equals the company average, so the label must be `'same'`.
- **One employee in a department:** The departmental average is simply that employee's payment, but it is still compared with every company payment in the period.
- **Several salary dates in one month:** This is the material trap in the exact source. Full-date partitions can produce separate statistics and contradictory duplicate month labels.
- **Missing employee record:** The foreign key excludes this case. With inconsistent data, the inner join would silently remove that salary from both averages.
- **Multiple employee rows for one identifier:** The employee primary key excludes this case. Otherwise the join would duplicate salary amounts and corrupt the averages.
- **Months with no salary rows:** They do not appear because there is no input evidence from which to form a department-month.
- **Result ordering:** The contract allows any order, so the absence of `ORDER BY` is intentional and harmless.
