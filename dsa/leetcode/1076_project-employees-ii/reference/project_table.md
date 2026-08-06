## Project Table

| Column Name | Type |
|---|---|
| `project_id` | int |
| `employee_id` | int |

The pair `(project_id, employee_id)` is the composite primary key, so one employee can appear at most once within a particular project. `employee_id` is a foreign key that references the `Employee` table. Each row records that the identified employee works on the identified project.
