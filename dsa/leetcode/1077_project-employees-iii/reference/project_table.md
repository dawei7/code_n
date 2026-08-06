## Project Table

| Column Name | Type |
|---|---|
| `project_id` | int |
| `employee_id` | int |

The pair `(project_id, employee_id)` is the table's composite primary key, so an employee can appear at most once within one project. `employee_id` is a foreign key that references `Employee`. Each row records that the identified employee works on the identified project.
