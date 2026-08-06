## Function Contract

**Inputs**

`Project(project_id, employee_id)` contains $R$ distinct project-employee assignments. `Employee(employee_id, name, experience_years)` contains $E$ employee records keyed by `employee_id`, and each assignment refers to one of those records.

**Return value**

- Return exactly the columns `project_id` and `employee_id`.
- For each project present in `Project`, include every assigned employee whose `experience_years` equals that project's maximum.
- Rank an employee independently in every project to which that employee is assigned.
- Do not use `name` to select or break ties.
- Result order is unrestricted; the local reference orders both output columns only to make validation deterministic.
