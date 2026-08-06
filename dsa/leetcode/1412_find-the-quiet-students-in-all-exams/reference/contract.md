## Function Contract

**Inputs**

- `Student(student_id, student_name)` contains $S$ students keyed by `student_id`.
- `Exam(exam_id, student_id, score)` contains $E$ exam-participation rows keyed by `(exam_id, student_id)`.

**Return value**

Return exactly the columns `student_id` and `student_name`. A returned student must have at least one row in `Exam`, and every one of that student's scores must be strictly greater than the minimum score and strictly less than the maximum score within its own exam. Consequently, a score tied at either extreme disqualifies the student, and the sole participant in an exam is both extremes.

One extreme result in any exam disqualifies an otherwise quiet student. Exclude students who never participated and order qualifying rows by `student_id`.
