## Function Contract

**Inputs**

`Salary(id, employee_id, amount, pay_date)` contains the dated payments, and `Employee(employee_id, department_id)` supplies each employee's department. Let $S$ and $E$ be the respective row counts.

**Return value**

Return one row for each department-month present in `Salary`:

- `pay_month`: the payment month formatted as `YYYY-MM`;
- `department_id`: the department being compared;
- `comparison`: `higher`, `lower`, or `same` relative to the average of every company payment in that same month.

Result order is unrestricted.
