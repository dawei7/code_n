## Examples

**Example 1**

- **Input:** `Student = [[1,"Daniel"],[2,"Jade"],[3,"Stella"],[4,"Jonathan"],[5,"Will"]], Exam = [[10,1,70],[10,2,80],[10,3,90],[20,1,80],[30,1,70],[30,3,80],[30,4,90],[40,1,60],[40,2,70],[40,4,80]]`

`Student`:

| student_id | student_name |
|---:|---|
| 1 | Daniel |
| 2 | Jade |
| 3 | Stella |
| 4 | Jonathan |
| 5 | Will |

`Exam`:

| exam_id | student_id | score |
|---:|---:|---:|
| 10 | 1 | 70 |
| 10 | 2 | 80 |
| 10 | 3 | 90 |
| 20 | 1 | 80 |
| 30 | 1 | 70 |
| 30 | 3 | 80 |
| 30 | 4 | 90 |
| 40 | 1 | 60 |
| 40 | 2 | 70 |
| 40 | 4 | 80 |

- **Output:** `[[2,"Jade"]]`

| student_id | student_name |
|---:|---|
| 2 | Jade |

- **Explanation:** In exam 10, students 1 and 3 have the lowest and highest scores. Student 1 is the only participant in exam 20, so that score is both extremes. In exams 30 and 40, students 1 and 4 hold the lowest and highest scores. Students 2 and 5 never have an extreme score, but student 5 never participates in an exam and must be excluded. Therefore only student 2 is returned.
