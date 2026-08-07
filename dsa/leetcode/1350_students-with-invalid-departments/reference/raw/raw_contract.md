## Function Contract

**Input**

- `Departments`: the current university-department table described above.
- `Students`: the student and recorded-department table described above.

Let $D$ be the number of department rows, $S$ the number of student rows, and $N=D+S$.

**Return value**

Return a table with these columns:

- `id`: the primary-key ID from an invalid student's `Students` row.
- `name`: that student's name from the same row.

A row qualifies exactly when its `department_id` does not equal the `id` of any current department. The result order is unrestricted.
