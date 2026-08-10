## General

**Group historical records by employee**

An employee can have several salary rows. Under the assumption that salary increases over time, the current salary is the greatest salary recorded for that employee.

The query groups rows with:

`GROUP BY emp_id`.

Each group represents one employee identifier. Aggregate `MAX(salary)` then chooses one greatest salary value from that employee's records.

**Select the requested columns**

The output projects:

- `emp_id`;
- `firstname`;
- `lastname`;
- maximum salary aliased back to `salary`;
- `department_id`.

`AS salary` ensures the aggregate result uses the required output column name rather than a generated expression label.

The query assumes name and department fields are stable across all historical rows for the same employee. Under that intended data model, selecting those nonaggregated values alongside the grouped identifier yields the employee details associated with the group.

**Why maximum represents latest**

No year or timestamp column exists. The problem supplies a semantic assumption instead: salaries increase each year.

If historical salary sequence is strictly or non-strictly increasing over time, its greatest numeric value is the most recent value.

Thus:

$$
\text{currentSalary}(e)
=
\max\{\text{salary from rows with emp\_id }e\}.
$$

The query uses this inference rather than attempting to infer row insertion order.

**Trace one employee**

Employee one has salary strings representing 110000 and 106119.

Grouping puts both rows in one employee group. Maximum is 110000, so the output retains one row for employee one with that salary.

Employees having one record form one-row groups; their maximum is simply that record.

**Order the final employee rows**

`ORDER BY emp_id` defaults to ascending order.

Ordering occurs after grouping, so it sorts one output row per employee rather than the raw historical records.

The result begins with the smallest identifier and proceeds upward exactly as required.

**A schema-sensitive detail: salary is declared `varchar`**

The table schema declares `salary` as text, not an integer. In MySQL, `MAX` applied directly to a character expression can compare values using string ordering rather than numeric magnitude.

For positive salary strings of the same digit length, lexicographic and numeric order agree, as they do in the shown data. If differently sized strings such as `"90000"` and `"100000"` were compared lexically, direct text maximum could select the wrong numeric salary.

The exact stored query does not cast. A schema-robust numeric version would use something like `MAX(CAST(salary AS UNSIGNED))`, possibly converting back to the expected type if necessary.

This explanation preserves the exact source while making its representation assumption explicit.

**Another MySQL detail: nonaggregated columns**

The query groups only by `emp_id` but selects `firstname`, `lastname`, and `department_id` without aggregates.

This works in permissive MySQL modes and is semantically safe when those attributes are constant for every row of one employee. Under strict `ONLY_FULL_GROUP_BY` without a recognized functional dependency, MySQL may reject the query.

A fully portable version could first calculate maximum salary per employee and join it back, or group by all stable employee-detail columns.

The accepted exact solution relies on the challenge's data consistency and MySQL execution environment.

**Logical correctness under the intended assumptions**

Partition `Salary` by `emp_id`. Each input row belongs to exactly one group. The aggregate returns one maximum salary per group.

The monotone-salary assumption makes that maximum current. Stable identity columns supply the same name and department no matter which group row provides them.

Finally, ascending identifier ordering produces the required deterministic order. Therefore, under those intended assumptions, each employee appears exactly once with current salary.

**Why row-by-row self-comparison is unnecessary**

One could use a correlated subquery to ask whether a larger salary exists for the same employee. Aggregation expresses the same maximum directly and lets the database optimizer choose hash or sort grouping.

No window rank is needed when only the maximum value and stable employee attributes are required.

**Primary-key implication**

The composite primary key $(\texttt{emp_id},\texttt{salary})$ prevents duplicate salary strings for the same employee. It does not by itself guarantee that name and department never change, but the narrative treats records as salary history for fixed employees.

The maximum aggregate would remain the same even if duplicate salary rows were allowed.

## Complexity detail

Let $R$ be the number of Salary rows and $E$ the number of employees.

The database must scan $R$ rows. Hash aggregation can group in expected $O(R)$ time, while sort-based grouping can take $O(R\log R)$. Ordering $E$ output rows costs $O(E\log E)$. A conservative engine-independent bound is $O(R\log R)$.

Grouping and sorting may use $O(E)$ to $O(R)$ working space, summarized as $O(R)$.

## Alternatives and edge cases

- **Numeric cast inside `MAX`:** Safer because `salary` is declared `varchar` and numeric order may differ from text order.
- **Window function `ROW_NUMBER`:** Rank rows per employee by numeric salary descending and keep rank one; useful when row-specific changing attributes must come from the winning record.
- **Aggregate subquery plus join:** Portable way to retrieve the row corresponding to each maximum salary.
- **One record for an employee:** It is automatically current.
- **Equal numeric text formats:** Direct string maximum agrees with numeric maximum when positive strings have equal length.
- **Different digit lengths:** Exact query may compare lexically; a cast is needed for robust numeric semantics.
- **Stable employee details:** Required for nonaggregated selected fields to be unambiguous.
- **Strict SQL mode:** May require grouping additional columns or a join.
- **Composite primary key:** Prevents the same employee-salary pair from repeating.
- **Output order:** Bare `ORDER BY emp_id` means ascending by default.
