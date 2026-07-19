## General
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

## Complexity detail
With indexed or hash-based equality joins, each table is scanned and probed in
$O(E+S)$ expected time. The union, join structures, and result can retain
$O(E+S)$ IDs, giving $O(E+S)$ working space. A database engine may choose a
different physical plan while preserving the query semantics.

## Alternatives and edge cases
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
