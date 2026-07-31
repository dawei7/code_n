## Employee Table

| Column Name | Type |
|---|---|
| `id` | int |
| `name` | varchar |
| `salary` | int |
| `departmentId` | int |

`id` is the primary key. `departmentId` references `Department.id`; each row stores an employee's identity, name, salary, and department.
