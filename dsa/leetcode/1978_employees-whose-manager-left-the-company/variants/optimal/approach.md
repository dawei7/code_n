## General

**Treat the table as both employees and possible managers**

Every manager who is still employed also has a row in `Employees` whose `employee_id` equals a report's `manager_id`. A manager who left has no such row, although the report retains the old ID. The problem is therefore an existence test against the same table.

The query aliases `Employees` as `e1` for the employee being considered and as `e2` for that employee's possible manager. The join condition

`e1.manager_id = e2.employee_id`

asks the database to find the manager row.

**Why a left join is necessary**

An inner join would retain only employees whose manager row exists. Those are precisely the employees that must be excluded, so an inner join would discard the desired evidence.

A `LEFT JOIN` retains every `e1` row. If a matching manager exists, columns from `e2` contain that manager's values. If none exists, all `e2` columns are SQL `NULL`. Because `employee_id` is a primary key and cannot itself be null in a real row, `e2.employee_id IS NULL` is a reliable unmatched-row test.

This pattern is called an anti-join: keep left-side rows for which no right-side match exists.

**Apply all three required filters**

`e1.salary < 30000` enforces the strict salary limit. A salary equal to 30000 does not qualify.

`e1.manager_id IS NOT NULL` distinguishes "had a manager whose row is gone" from "does not have a manager." Without this condition, a top-level employee's null manager ID would fail to match any `e2` row and would incorrectly look like a departed manager.

`e2.employee_id IS NULL` then proves that the nonnull recorded manager ID is absent from the current table.

The three predicates together express the contract exactly: low salary, an actual recorded manager ID, and no current employee row for that manager.

**Trace the example**

Employee 1 has salary 21241 and manager 11. The left join finds employee 11, so `e2.employee_id` is 11 rather than null. Employee 1 is excluded because the manager is still present.

Employee 11 has salary 28485 and manager 6. There is no employee row with ID 6, so the left join produces null right-side columns. The manager ID itself is nonnull, all three conditions pass, and employee 11 is returned.

Employees 12 and 13 have null manager IDs. Even if their salaries were low, the explicit manager-null condition would exclude them because no-manager is not the same as manager-left.

**Why no duplicate elimination is needed**

`employee_id` is the primary key of `Employees`. Therefore at most one `e2` row can match a given `manager_id`, and each `e1` employee produces at most one joined result. Selecting `e1.employee_id` cannot create duplicates, so `DISTINCT` is unnecessary.

**Order by the selected column**

The contract requires ascending employee ID. `ORDER BY 1` means order by the first expression in the select list, which is `e1.employee_id`. It is a concise positional form of `ORDER BY e1.employee_id`.

Using the explicit name can be easier to maintain if the select list later changes, but both forms have the same meaning in this exact one-column query.

**Why the query is correct**

For any returned row, the salary predicate proves the employee earns strictly less than 30000, the nonnull predicate proves a manager was recorded, and the unmatched right row proves that manager ID has no current employee record. Thus every returned employee qualifies.

For any qualifying employee, its row appears as `e1`, its salary and nonnull manager pass the first two checks, and the departed manager has no matching `e2` row. The left join preserves the employee with a null right side, so the final check passes. Thus every qualifying employee is returned. Primary-key uniqueness returns each exactly once, and the final ordering satisfies the presentation requirement.

## Complexity detail

Let $R$ be the number of employee rows. The database scans candidate employee rows and performs manager-existence lookups. With a hash anti-join, expected time and working space are $O(R)$, matching the manifest. With the primary-key B-tree used for repeated lookups, a possible plan is $O(R\log R)$ time and smaller extra memory. SQL complexity depends on the optimizer and indexes rather than being fixed solely by query text.

The final ordering of up to $R$ qualifying IDs can require $O(R\log R)$ comparison time and $O(R)$ temporary space unless an index/order-preserving plan supplies the rows already sorted. The query's logical filtering work remains linear under a hash plan.

## Alternatives and edge cases

- **`NOT EXISTS` correlated subquery:** Expresses the anti-join directly and is often optimized to a similar execution plan.
- **`NOT IN` subquery:** It is concise but can have surprising three-valued-logic behavior when nulls are possible; `NOT EXISTS` or left anti-join is clearer.
- **Inner join:** Incorrectly preserves managers who still exist and discards employees whose manager left.
- **Missing `manager_id IS NOT NULL` check:** Would misclassify employees who never had a manager as having a departed manager.
- **Salary exactly 30000:** Excluded because the comparison is strict.
- **Manager still employed:** A matching `e2` primary key makes the null test false.
- **Departed manager:** The retained nonnull ID has no match, so the left-joined key is null.
- **Several employees share one departed manager:** Each qualifying low-salary report is returned independently.
- **Primary-key uniqueness:** Prevents one employee from acquiring duplicate joined manager rows.
- **Null comparison:** Use `IS NOT NULL` and `IS NULL`; equality comparisons with SQL `NULL` do not evaluate to true.
- **Required ordering:** `ORDER BY 1` sorts the sole result column in ascending order by default.
- **No table mutation:** The query only reads `Employees`.
