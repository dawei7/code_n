## General

**Use two roles of the same employee table**

Every direct-report relationship is stored in one employee row: `reports_to` contains that employee's manager ID. Manager identity and name are stored in another row of the same table.

The query therefore uses a self-join:

- `e1` represents reporting employees.
- `e2` represents their managers.

The condition `e1.reports_to = e2.employee_id` pairs each report with the employee row for that report's manager.

**Why an inner join returns only managers**

An employee is a manager for this problem only if at least one other employee reports directly to them. Such an employee appears as `e2` in at least one joined pair.

Employees with no reports produce no joined rows and are absent automatically. Employees whose `reports_to` is null also do not match a manager row as `e1`, which is correct because they are not direct reports of anyone.

No separate `HAVING COUNT > 0` is needed because every output group is created from at least one successful join.

**Group report rows by manager**

`GROUP BY 1` groups by the first select expression, `e2.employee_id`. Since `employee_id` is unique, each group corresponds to one manager.

`e2.name` is functionally determined by that unique employee ID. MySQL can project the manager's name alongside the grouped key without creating separate groups for duplicate names. Two managers may share a name but remain separate because their IDs differ.

**Count direct reports**

`COUNT(1) AS reports_count` counts every joined employee-manager row in the group. Each `e1` row represents one employee directly reporting to that manager, so the row count is the number of direct reports.

The query does not recursively include reports of reports. For example, if Charlie reports to Alice and Alice reports to Michael, Charlie contributes to Alice's group, not Michael's. This matches the word “directly.”

**Average only the reports' ages**

`AVG(e1.age)` uses ages from the reporting-employee alias, not the manager alias. It sums all direct-report ages in the manager's group and divides by `reports_count`.

`ROUND(...) AS average_age` rounds that average to the nearest integer according to MySQL's numeric rounding behavior. For positive exact ages, a half such as 38.5 rounds to 39, matching the example.

The manager's own age is never included unless that row somehow reports to itself; ordinary hierarchy data does not do so.

**Trace the first example**

Alice's row and Bob's row both have `reports_to = 9`. The join matches each to Hercy's manager row with employee ID nine.

The group for nine contains two joined rows, so `COUNT(1)` is two. Their ages are 41 and 36, producing average 38.5 and rounded value 39.

Winston has no direct reports and never appears as `e2` in the join, so no output row is produced for him.

**Order managers by ID**

`ORDER BY 1` sorts by the first projected expression, `e2.employee_id`, in ascending order by default.

Grouping does not promise presentation order, so this explicit clause is required by the contract.

**Why the query is correct**

Fix a manager $M$. The join creates exactly one row for each employee whose `reports_to` equals $M$'s unique ID, paired with $M$'s identity row. No indirect report qualifies because its `reports_to` names a different immediate manager.

Grouping collects exactly those rows. Their count is the number of direct reports, and their `e1.age` average is exactly the required average report age. A group exists if and only if at least one such employee exists, which is precisely the manager definition.

The selected ID and name come from $M$, and final sorting changes only row order. Every required manager appears once with correct aggregates.

**Why employee ID alone is a sufficient group key**

The schema guarantees `employee_id` uniqueness, so one ID maps to one manager row and one name. Grouping additionally by name would be valid but redundant.

This functional dependency matters under strict SQL grouping rules. MySQL recognizes primary or unique key dependencies in normal configurations; explicitly grouping by both projected manager columns is a portable alternative.

## Complexity detail

Let $E$ be the number of employee rows and $M$ the number of managers with reports. With a hash lookup or index on the unique manager ID, the self-join and aggregation can process rows in expected $O(E)$ time while storing $O(M)$ group states, matching the manifest.

The final `ORDER BY` may require $O(M\log M)$ time and $O(M)$ temporary space if the groups are not already produced in ID order. Indexed or sort-based plans vary, so the manifest's $O(E)$ is the logical join-and-aggregation bound rather than a guarantee for every physical plan.

The output contains $M$ rows.

## Alternatives and edge cases

- **Group by `reports_to` then join:** Aggregate report counts and ages first, then join the smaller manager summary to Employees for names. It is logically equivalent.
- **Correlated subqueries:** Count and average reports separately for every employee. Without good indexing, this repeats work.
- **Left self-join:** It would include nonmanagers unless filtered with `HAVING COUNT(e1.employee_id)>0`; the inner join naturally excludes them.
- **One direct report:** Count is one and average age equals that report's age.
- **Several hierarchy levels:** Only rows naming the manager directly enter the group.
- **Top-level employee:** A null `reports_to` does not make someone a report, but they can still appear as a manager through other rows.
- **Same manager names:** Unique IDs keep their groups separate.
- **Manager's own age:** It is excluded because averaging uses `e1.age`.
- **Half-value average:** MySQL `ROUND` produces the required nearest integer for positive ages.
- **No reports:** The employee has no joined group and is not returned.
- **Invalid manager reference outside the stated relational model:** An inner join would omit that reporting row because no manager identity exists.
- **Ordinal clauses:** `GROUP BY 1` and `ORDER BY 1` rely on manager ID remaining the first select expression.
- **Functional dependency:** Manager name is fixed by unique employee ID, allowing it to be selected with that group key.
