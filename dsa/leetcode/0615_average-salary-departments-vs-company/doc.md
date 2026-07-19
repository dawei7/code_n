# Average Salary: Departments VS Company

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 615 |
| Difficulty | Hard |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/average-salary-departments-vs-company/) |

## Problem Description
### Goal
Given employee-department assignments and dated salary payments, compare each department's average salary with the average salary of the entire company for the same month. Treat a month as the `YYYY-MM` portion of `pay_date`, and use only payments made in that month for both averages.

Return `pay_month`, `department_id`, and a column named `comparison` for every department-month represented in the salary data. Set `comparison` to `higher`, `lower`, or `same` according to how the department average relates to the company-wide average for that month; months and departments must not be mixed across comparison groups.

### Function Contract
**Inputs**

- `Salary(id, employee_id, amount, pay_date)`: dated salary payments
- `Employee(employee_id, department_id)`: each employee's department

**Return value**

- `pay_month`: the payment month formatted as `YYYY-MM`
- `department_id`: the department being compared
- `comparison`: `higher`, `lower`, or `same` relative to the company average in that month

### Examples
**Example 1**

- Input: in March, department 1 averages `9000`, department 2 averages `8000`, and the company averages about `8333.33`
- Output: department 1 is `higher`; department 2 is `lower`

**Example 2**

- Input: in February, both departments and the company average `7000`
- Output: both departments are `same`
