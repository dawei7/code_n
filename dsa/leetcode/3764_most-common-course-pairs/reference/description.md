## Description

Table: `course_completions`

```

+-------------------+---------+
| Column Name       | Type    | 
+-------------------+---------+
| user_id           | int     |
| course_id         | int     |
| course_name       | varchar |
| completion_date   | date    |
| course_rating     | int     |
+-------------------+---------+
(user_id, course_id) is the combination of columns with unique values for this table.
Each row represents a completed course by a user with their rating (1-5 scale).

```

Write a solution to identify **skill mastery pathways** by analyzing course completion sequences among top-performing students:

<ul>
	<li>Consider only **top-performing students** (those who completed **at least **`5`** courses** with an **average rating of **`4`** or higher**).</li>
	<li>For each top performer, identify the **sequence of courses** they completed in chronological order.</li>
	<li>Find all **consecutive course pairs** (`Course A → Course B`) taken by these students.</li>
	<li>Return the **pair frequency**, identifying which course transitions are most common among high achievers.</li>
</ul>

Return *the result table ordered by* *pair frequency in **descending** order* *and then by first course name and second course name in **ascending** order*.

The result format is in the following example.
