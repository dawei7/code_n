## Description

The `Salary` table stores one or more yearly salary records for each employee. Older rows may therefore contain amounts that are no longer current. Salaries are guaranteed to increase from year to year, so an employee's latest record is the row having that employee's greatest numeric salary.

Return one current row per employee with `emp_id`, `firstname`, `lastname`, `salary`, and `department_id`. Sort the result by `emp_id` in ascending order. Employees having only one stored record must still appear, because that row is already their latest salary.
