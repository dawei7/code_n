## Function Contract

**Inputs**

- `SchoolA`: Table with columns `student_id` (int), `student_name` (varchar).
- `SchoolB`: Table with columns `student_id` (int), `student_name` (varchar).
- `SchoolC`: Table with columns `student_id` (int), `student_name` (varchar).

**Return value**

Return a table with columns `member_A`, `member_B`, and `member_C` representing all valid combinations of one student from each school where all 3 `student_id`s are pairwise distinct and all 3 `student_name`s are pairwise distinct.
