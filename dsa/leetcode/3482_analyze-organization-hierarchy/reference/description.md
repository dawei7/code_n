## Description

Table: `Employees`

```

+----------------+---------+
| Column Name    | Type    | 
+----------------+---------+
| employee_id    | int     |
| employee_name  | varchar |
| manager_id     | int     |
| salary         | int     |
| department     | varchar |
+----------------+----------+
employee_id is the unique key for this table.
Each row contains information about an employee, including their ID, name, their manager's ID, salary, and department.
manager_id is null for the top-level manager (CEO).

```

Write a solution to analyze the organizational hierarchy and answer the following:

<ol>
	<li>**Hierarchy Levels:** For each employee, determine their level in the organization (CEO is level `1`, employees reporting directly to the CEO are level `2`, and so on).</li>
	<li>**Team Size:** For each employee who is a manager, count the total number of employees under them (direct and indirect reports).</li>
	<li>**Salary Budget:** For each manager, calculate the total salary budget they control (sum of salaries of all employees under them, including indirect reports, plus their own salary).</li>
</ol>

Return *the result table ordered by <em>the result ordered by **level** in **ascending** order, then by **budget** in **descending** order, and finally by **employee_name** in **ascending** order*.</em>

*The result format is in the following example.*
