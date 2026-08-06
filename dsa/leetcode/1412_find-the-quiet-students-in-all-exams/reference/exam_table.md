## Exam Table

| Column Name | Type |
|---|---|
| `exam_id` | int |
| `student_id` | int |
| `score` | int |

The pair `(exam_id, student_id)` is the table's composite primary key, so a student has at most one score in a particular exam. Each row records the number of points earned by the identified student in the identified exam.
