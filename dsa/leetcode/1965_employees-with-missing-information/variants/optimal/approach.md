## General

**Missing information is a symmetric difference of IDs**

An employee has complete information only when their ID appears in both `Employees` and `Salaries`. Missing information means the ID appears in exactly one table:

- present in `Employees` but absent from `Salaries` means salary is missing;
- present in `Salaries` but absent from `Employees` means name is missing.

The query computes these two directions separately and unions them.

**Find employees without salaries**

The first SELECT starts from `Employees` and keeps rows whose ID is not among IDs returned by `Salaries`:

`employee_id NOT IN (SELECT employee_id FROM Salaries)`.

Every surviving ID has a name row but no salary row.

**Find salaries without employees**

The second SELECT reverses the tables. It starts from `Salaries` and retains IDs absent from `Employees`. Every survivor has a salary but no name.

`UNION` combines the two result sets and performs duplicate elimination. Logically the sets are disjoint—an ID cannot simultaneously be “only in Employees” and “only in Salaries”—so `UNION ALL` would yield the same values under the schema. `UNION` is still safe and directly expresses a set symmetric difference.

**Sort by the required column**

`ORDER BY 1` orders by the first selected expression, `employee_id`, in ascending order by default. It applies to the complete union result, not just the second SELECT.

For the sample, ID two survives the first branch because it lacks a salary; ID one survives the second because it lacks an employee-name row. IDs four and five exist in both subqueries' comparison sets and are excluded.

**Why the query is correct**

If an ID is returned by the first branch, exactly the salary side is absent; if returned by the second, exactly the employee side is absent. In either case its required information is missing.

Conversely, any missing-information ID must lack at least one of the two table rows. If it has an employee row but lacks salary, the first branch returns it. If it has salary but lacks employee, the second returns it. An ID absent from both tables does not describe a known employee and cannot appear in any input-driven result, which is appropriate.

IDs in both tables fail both `NOT IN` predicates and are omitted. The union plus ordering therefore produces exactly the required report.

**Null semantics and the schema contract**

SQL `NOT IN` has special behavior if its subquery contains `NULL`: comparisons can become unknown. The problem models `employee_id` as the unique identifier in each table and intends real IDs, so the solution relies on non-null identifier semantics. In a nullable schema, `NOT EXISTS` would be safer.

The query detects missing rows, not a null `name` or `salary` inside an existing row. The provided table contract represents information through the presence of unique ID rows.

**Follow the sample IDs through both branches**

`Employees` contains IDs two, four, and five, while `Salaries` contains one, four, and five. In the first branch, two is not in the salary subquery and survives; four and five are found and fail the predicate. In the second branch, one is absent from Employees and survives; four and five fail again. `UNION` produces IDs one and two, and the final ordering places one first.

This branch-level trace also shows why an ordinary inner join is the opposite of what is needed: an inner join would retain four and five, the complete records, and discard exactly the incomplete IDs being requested.

**Why both anti-join directions are necessary**

A left anti-join from Employees alone can discover missing salaries but has no row from which to discover an ID that exists only in Salaries. Reversing the direction finds the other category. Their union is the complete symmetric difference.

The query selects only `employee_id`, so there is no need to manufacture null placeholder columns for missing names or salaries.

## Complexity detail

Let $E$ and $S$ be the row counts of `Employees` and `Salaries`.

With hash sets or indexes for the subquery IDs, both anti-membership checks can be evaluated in $O(E+S)$ expected time. Sorting the output adds $O(R\log R)$ for $R$ missing IDs. The manifest's $O(E+S)$ summary treats identifier lookup and required output ordering under the intended indexed execution model; an explicit plan-sensitive bound includes sorting.

Materialized ID sets and union results can use $O(E+S)$ space. Actual SQL execution depends on indexes and the optimizer.

## Alternatives and edge cases

- **Two `NOT EXISTS` branches:** They express anti-joins and avoid `NULL` pitfalls associated with `NOT IN`.
- **Full outer join:** Join on employee ID and keep rows where either side is null. MySQL lacks direct full outer join syntax, so it must be simulated.
- **Left join plus right join:** Union two outer-join directions and filter missing sides. It is more verbose but equivalent.
- **ID in both tables:** It fails both anti-membership tests and is correctly omitted.
- **ID only in Employees:** It appears once as missing salary.
- **ID only in Salaries:** It appears once as missing name.
- **Both tables empty:** Both branches are empty and the ordered result is empty.
- **Empty Salaries table:** Every Employees ID is returned by the first branch.
- **Empty Employees table:** Every Salaries ID is returned by the second branch.
- **Duplicate elimination:** Unique IDs and disjoint branch meanings make duplicates impossible, but `UNION` safely enforces set output.
- **Inner join:** It would return complete employees rather than incomplete ones and is therefore unsuitable.
- **One anti-join direction:** It catches only one missing-information category; both are required.
- **Ascending order:** `ORDER BY 1` uses the sole selected column and defaults to ascending.
- **Nullable IDs:** A different schema allowing null identifiers should prefer `NOT EXISTS`.
