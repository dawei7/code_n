## Function Contract

**Input tables**

- `Project(project_id, employee_id)`: the employee-to-project assignments.
- `Employee(employee_id, name, experience_years)`: the referenced employee information.

The output grain is one row per project tied for the greatest assignment count. Because each `(project_id, employee_id)` pair is unique, counting `Project` rows for a project counts its distinct assigned employees. Employee names and experience values do not affect that count.

**Return value**

- One column named `project_id`.
- Every project identifier whose number of assignments is the maximum over all represented projects.
- Result order is unrestricted.
