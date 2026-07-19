# Employees With Missing Information

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1965 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/employees-with-missing-information/) |

## Problem Description
### Goal
The `Employees` table associates an employee ID with a name, while the
`Salaries` table associates an employee ID with a salary. Each table contains
at most one row for a given employee ID.

An employee has missing information when their ID appears in exactly one of
the two tables: a row found only in `Employees` lacks salary information, and
a row found only in `Salaries` lacks a name. Report every such employee ID in
ascending numeric order.

### Function Contract
**Inputs**

- `Employees(employee_id, name)`: $E$ rows with unique `employee_id` values.
- `Salaries(employee_id, salary)`: $S$ rows with unique `employee_id` values.

**Return value**

- A table with one column, `employee_id`.
- Include IDs present in exactly one input table.
- Order rows by `employee_id` ascending.

### Examples
**Example 1**

`Employees` contains IDs 2, 4, and 5; `Salaries` contains IDs 1, 4, and 5.

- Output rows: `(1)` and `(2)`, in that order.

**Example 2**

Both tables contain exactly IDs 3 and 8.

- Output: no rows.

**Example 3**

`Employees` contains ID 7 and `Salaries` is empty.

- Output row: `(7)`.

### Required Complexity
- **Time:** $O(E+S)$
- **Space:** $O(E+S)$

<details>
<summary>Approach</summary>

#### General

**Find employees without salary rows**

Left-join `Employees` to `Salaries` on `employee_id`. When no salary row
matches, the joined salary-side ID is `NULL`; select the employee-side ID from
exactly those rows. Uniqueness of IDs prevents duplicates within this branch.

**Find salaries without employee rows**

Perform the symmetric left anti-join from `Salaries` to `Employees`. Combine
the two missing-ID sets with `UNION` and order the result. An ID in both tables
is rejected by both anti-joins, while an ID in only one table is selected by
exactly its corresponding branch. These cases exhaust the symmetric
difference, so the result contains precisely the employees with missing
information.

#### Complexity detail

With indexed or hash-based equality joins, each table is scanned and probed in
$O(E+S)$ expected time. The union, join structures, and result can retain
$O(E+S)$ IDs, giving $O(E+S)$ working space. A database engine may choose a
different physical plan while preserving the query semantics.

#### Alternatives and edge cases

- **Full outer join:** Filter rows whose name-side or salary-side match is
  absent. This expresses the symmetric difference directly, but MySQL does not
  provide a native full outer join.
- **`NOT IN` subqueries:** Two set-difference branches can be concise, but
  nullable subquery values can make `NOT IN` semantics surprising; anti-joins
  avoid that trap.
- IDs present in both tables are complete and must not appear.
- A table may contribute several missing IDs, and both tables may contribute
  IDs in the same result.
- Source row order is irrelevant; the final `ORDER BY` owns the required
  ascending order.

</details>
