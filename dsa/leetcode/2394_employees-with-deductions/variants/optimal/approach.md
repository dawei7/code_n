## General

**Preserve employees who never logged a session.** The report begins with
`Employees` and left-joins `Logs` by `employee_id`. An inner join would erase
an employee with no log rows even though that employee has worked zero minutes
and must be considered for a deduction. Grouping by the employee identifier
and required hours then produces one result group for every employee.

**Round at the session boundary.** For each matched log, compute the exact
elapsed seconds with `TIMESTAMPDIFF`, divide by 60, and apply `CEIL`. This
rounding occurs before `SUM`, as required. Rounding the total duration after
adding raw seconds would be different: two sessions of 30 minutes 1 second
must contribute 31 minutes each, not 61 minutes in total.

**Compare one unit against another.** Convert `needed_hours` to minutes by
multiplying it by 60. For an employee without logs, the aggregate is `NULL`,
so `COALESCE(..., 0)` supplies the correct zero-minute total. The `HAVING`
clause retains precisely the groups whose credited minutes are strictly less
than their required minutes. Equality is deliberately excluded because an
employee who exactly meets the requirement is not deducted.

Every employee contributes exactly one group. Every real log in that group
contributes its independently rounded duration exactly once, and the null row
created by the left join contributes no duration. Consequently the aggregate
is the contract's credited work total, and the strict comparison selects
exactly the required employee identifiers.

## Complexity detail

Let $E$ be the number of `Employees` rows and $L$ the number of `Logs` rows. A
conservative sort-based join and grouping plan takes
$O((E + L)\log(E + L))$ time and $O(E + L)$ auxiliary space. With suitable
indexes or hash tables, a database engine can commonly execute the join and
aggregation in expected $O(E + L)$ time, but that physical-plan optimization
is not required by the stated bound.

## Alternatives and edge cases

- **Pre-aggregate logs:** First total rounded minutes by `employee_id`, then
  left-join that smaller result to `Employees`; it is equally correct and can
  reduce the join's intermediate rows.
- **Correlated aggregate:** A subquery can sum logs separately for every
  employee, but without a useful index it may rescan all $L$ sessions for each
  of the $E$ employees and approach $O(EL)$ work.
- **Inner join:** Starting with an inner join is shorter but incorrectly omits
  employees who have no logs.
- **Rounding after summation:** Applying `CEIL` only after summing seconds
  loses the required per-session rounding and can undercount credited time.
- **Crossing midnight:** Timestamp subtraction must use the full date and time;
  subtracting only clock fields would make an overnight session negative.
- **Exact threshold:** An employee whose rounded total equals
  `needed_hours * 60` meets the requirement, so the comparison is strict `<`.
- **Result order:** No `ORDER BY` is necessary because any row order is valid.
