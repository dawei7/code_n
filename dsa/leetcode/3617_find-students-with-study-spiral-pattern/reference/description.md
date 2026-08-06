## Description

Table: `students`

```

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| student_name | varchar |
| major        | varchar |
+--------------+---------+
student_id is the unique identifier for this table.
Each row contains information about a student and their academic major.

```

Table: `study_sessions`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| session_id    | int     |
| student_id    | int     |
| subject       | varchar |
| session_date  | date    |
| hours_studied | decimal |
+---------------+---------+
session_id is the unique identifier for this table.
Each row represents a study session by a student for a specific subject.

```

Write a solution to find students who follow the **Study Spiral Pattern** - students who consistently study multiple subjects in a rotating cycle.

<ul>
	<li>A Study Spiral Pattern means a student studies at least `3`** different subjects** in a repeating sequence</li>
	<li>The pattern must repeat for **at least **`2`** complete cycles** (minimum `6` study sessions)</li>
	<li>Sessions must be **consecutive dates** with no gaps longer than `2` days between sessions</li>
	<li>Calculate the **cycle length** (number of different subjects in the pattern)</li>
	<li>Calculate the **total study hours** across all sessions in the pattern</li>
	<li>Only include students with cycle length of **at least **`3`** subjects**</li>
</ul>

Return *the result table ordered by cycle length in **descending** order, then by total study hours in **descending** order*.

The result format is in the following example.
