## General
**Attach experience before comparing assignments:** Join `Project` with `Employee` on `employee_id`. Each assignment then carries the experience value that must be compared only with other assignments in the same project.

**Rank within each project:** Apply `DENSE_RANK()` partitioned by `project_id` and ordered by `experience_years` descending. The greatest value receives rank one. Dense rank deliberately assigns the same rank to equal experience values, so it does not discard tied employees.

**Keep the complete top rank:** Select every row whose computed rank is one and return only `project_id` and `employee_id`. For each project, no employee with smaller experience can receive rank one, while every employee whose experience equals the project maximum does receive rank one. The filter therefore returns exactly the required employees for every project.

## Complexity detail
A hash join can build an $E$-row employee lookup and attach experience in expected $O(E+R)$ time. Partitioning and ordering the $R$ joined assignments for the window function takes $O(R\log R)$ time in a sort-based plan. The join state, sorted rows, and window result use up to $O(E+R)$ execution space; indexes and the optimizer may alter the physical plan.

## Alternatives and edge cases
- **Grouped maximum then join back:** Compute `MAX(experience_years)` per project and join that result to the assignments. It is also efficient and naturally preserves ties, but requires a second relational step to recover employee identifiers.
- **Correlated project maximum:** Recompute the maximum for each assignment. It is correct but can repeatedly rescan assignments and approach quadratic time.
- **`ROW_NUMBER()`:** It arbitrarily chooses one row among equal experience values and is incorrect when the maximum is tied.
- **Tied experience:** Every employee tied at the project maximum must appear.
- **Employee on several projects:** The employee is ranked independently within each project's partition.
- **Single assignment:** That employee is necessarily the most experienced for the project.
- **Employee name:** Names do not participate in either the join identity or the experience comparison.
