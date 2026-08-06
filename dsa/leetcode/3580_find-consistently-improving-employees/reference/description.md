## Description

Table: `employees`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
+-------------+---------+
employee_id is the unique identifier for this table.
Each row contains information about an employee.

```

Table: `performance_reviews`

```

+-------------+------+
| Column Name | Type |
+-------------+------+
| review_id   | int  |
| employee_id | int  |
| review_date | date |
| rating      | int  |
+-------------+------+
review_id is the unique identifier for this table.
Each row represents a performance review for an employee. The rating is on a scale of 1-5 where 5 is excellent and 1 is poor.

```

Write a solution to find employees who have consistently improved their performance over **their last three reviews**.

<ul>
	<li>An employee must have **at least **`3`** review** to be considered</li>
	<li>The employee's **last **`3`** reviews** must show **strictly increasing ratings** (each review better than the previous)</li>
	<li>Use the most recent `3` reviews based on `review_date` for each employee</li>
	<li>Calculate the **improvement score** as the difference between the latest rating and the earliest rating among the last `3` reviews</li>
</ul>

Return *the result table ordered by **improvement score** in **descending** order, then by **name** in **ascending** order*.

The result format is in the following example.
