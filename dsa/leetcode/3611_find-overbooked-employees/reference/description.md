## Description

Table: `employees`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| employee_id   | int     |
| employee_name | varchar |
| department    | varchar |
+---------------+---------+
employee_id is the unique identifier for this table.
Each row contains information about an employee and their department.

```

Table: `meetings`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| meeting_id    | int     |
| employee_id   | int     |
| meeting_date  | date    |
| meeting_type  | varchar |
| duration_hours| decimal |
+---------------+---------+
meeting_id is the unique identifier for this table.
Each row represents a meeting attended by an employee. meeting_type can be 'Team', 'Client', or 'Training'.

```

Write a solution to find employees who are **meeting-heavy** - employees who spend more than `50%` of their working time in meetings during any given week.

<ul>
	<li>Assume a standard work week is `40`** hours**</li>
	<li>Calculate **total meeting hours** per employee **per week** (**Monday to Sunday**)</li>
	<li>An employee is meeting-heavy if their weekly meeting hours `>` `20` hours (`50%` of `40` hours)</li>
	<li>Count how many weeks each employee was meeting-heavy</li>
	<li>**Only include** employees who were meeting-heavy for **at least **`2`** weeks**</li>
</ul>

Return *the result table ordered by the number of meeting-heavy weeks in **descending** order, then by employee name in **ascending** order*.

The result format is in the following example.
