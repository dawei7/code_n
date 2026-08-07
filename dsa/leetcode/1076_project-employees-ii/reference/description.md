## Description

Table: `Project`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
(project_id, employee_id) is the primary key (combination of columns with unique values) of this table.
employee_id is a foreign key (reference column) to Employee table.
Each row of this table indicates that the employee with employee_id is working on the project with project_id.
```

Table: `Employee`

```
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
employee_id is the primary key (column with unique values) of this table.
Each row of this table contains information about one employee.
```

Write a solution to report all the **projects** that have the most employees.

Return the result table in **any order**.

The result format is in the following example.
### Function Contract

**Input tables**

- $Project(\text{project}_{id}, \text{employee}_{id})$: the employee-to-project assignments.
- $Employee(\text{employee}_{id}, name, \text{experience}_{years})$: the referenced employee information.

The output grain is one row per project tied for the greatest assignment count. Because each $(\text{project}_{id}, \text{employee}_{id})$ pair is unique, counting `Project` rows for a project counts its distinct assigned employees. Employee names and experience values do not affect that count.

**Return value**

- One column named $\text{project}_{id}$.
- Every project identifier whose number of assignments is the maximum over all represented projects.
- Result order is unrestricted.

### Examples

#### Example 1

```
**Input:**
Project table:
+-------------+-------------+
| project_id  | employee_id |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 1           | 3           |
| 2           | 1           |
| 2           | 4           |
+-------------+-------------+
Employee table:
+-------------+--------+------------------+
| employee_id | name   | experience_years |
+-------------+--------+------------------+
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 1                |
| 4           | Doe    | 2                |
+-------------+--------+------------------+
**Output:**
+-------------+
| project_id  |
+-------------+
| 1           |
+-------------+
**Explanation:** The first project has 3 employees while the second one has 2.
```