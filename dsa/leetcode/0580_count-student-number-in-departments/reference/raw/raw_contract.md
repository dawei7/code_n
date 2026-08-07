## Function Contract

**Inputs**

`Student(student_id, student_name, gender, dept_id)` contains the student records, and `Department(dept_id, dept_name)` contains the complete department catalog. Let $S$ and $D$ be their respective row counts.

**Return value**

Return one row per department with columns `dept_name` and `student_number`. Sort by the count from greatest to least, then by `dept_name` in ascending alphabetical order.
