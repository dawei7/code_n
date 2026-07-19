## General
The maximum is scoped to each department, and ties must be preserved. Partition employees by `departmentId`, order each partition by salary descending, and assign `DENSE_RANK`. Every employee at that department's maximum receives rank one.

Filter to rank one only after the window has been evaluated, typically through a common table expression or derived table. Window results are not available to the same query block's `WHERE` clause because filtering happens earlier in SQL's logical evaluation order.

Join the retained employees to `Department` to obtain the required department name, and project department name, employee name, and salary with the requested aliases. Partition by the stable department identifier rather than only its display name; two departments could theoretically share a name without being the same group.

For a department with salaries `90, 90, 80`, both employees earning `90` receive rank one and both appear. `ROW_NUMBER()` would arbitrarily keep only one if filtered to one, while `RANK()` or `DENSE_RANK()` both preserve the top tie; dense rank communicates the per-level intent clearly.

Within a department partition, descending ranking assigns rank one exactly to rows whose salary equals the partition maximum. Thus every filtered employee earns the highest salary in that employee's department. Conversely, every employee tied at the maximum appears at the first ordering level and receives rank one, so none is omitted. Joining on the department identifier attaches the correct department name without changing qualification.

## Complexity detail
Absent a useful index, partition ordering across `n` employee rows requires $O(n \log n)$ total work and may use $O(n)$ window/sort storage. An index beginning with `departmentId` and salary may improve the plan. Joining department names is typically linear or indexed and does not change the dominant bound.

## Alternatives and edge cases
- Aggregating `MAX(salary)` by department and joining those maxima back to `Employee` is portable, efficient, and naturally preserves ties.
- A correlated maximum subquery is compact but can repeat work unless the optimizer decorrelates it.
- `ROW_NUMBER()` is incorrect because it chooses one arbitrary employee from a tie.
- Single-employee departments return that employee. Departments with no employees produce no row.
- Any number of employees may share the maximum and all must be returned.
