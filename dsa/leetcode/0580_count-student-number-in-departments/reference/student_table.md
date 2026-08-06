## Student Table

| Column Name | Type |
|---|---|
| `student_id` | int |
| `student_name` | varchar |
| `gender` | varchar |
| `dept_id` | int |

`student_id` is the primary key, so its values are unique. `dept_id` is a foreign key referencing `Department.dept_id`. Each row records a student's name, gender, and department identifier.
