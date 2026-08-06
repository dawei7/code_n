## Examples

**Example 1**

- **Input:** `Student = [[1,"Jack","M",1],[2,"Jane","F",1],[3,"Mark","M",2]], Department = [[1,"Engineering"],[2,"Science"],[3,"Law"]]`

Student:

| student_id | student_name | gender | dept_id |
|---:|---|---|---:|
| 1 | Jack | M | 1 |
| 2 | Jane | F | 1 |
| 3 | Mark | M | 2 |

Department:

| dept_id | dept_name |
|---:|---|
| 1 | Engineering |
| 2 | Science |
| 3 | Law |

- **Output:** `[["Engineering",2],["Science",1],["Law",0]]`

| dept_name | student_number |
|---|---:|
| Engineering | 2 |
| Science | 1 |
| Law | 0 |
