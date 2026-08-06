## Employees Table

| Column Name | Type |
|---|---|
| `employee_id` | `int` |
| `employee_name` | `varchar` |
| `manager_id` | `int` |

`employee_id` contains unique values. Each row identifies an employee, gives that employee's name, and records the `employee_id` of the employee's direct manager in `manager_id`.

The head of the company has `employee_id = 1`.
