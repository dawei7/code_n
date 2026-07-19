## General
**Construct the required result domain**

Cross join `Students` with `Subjects`. This produces exactly one row for every required pair before attendance is considered, so students who never attended an exam and subjects they never attempted cannot disappear.

**Attach and count attendance records**

Left join `Examinations` on both `student_id` and `subject_name`. A pair with attendances expands to one joined row per recorded attempt, while a pair with none retains one row whose examination columns are `NULL`. Group by the student and subject fields, and count a nullable column from `Examinations`; `COUNT(column)` ignores that synthetic `NULL`, producing zero rather than one for missing attendance.

Every examination row joins only to its exact student-subject pair, so duplicates contribute individually to that pair's count. Conversely, the initial cross product guarantees every pair has a group even without a match. Ordering the grouped rows by the two required keys completes the contract.

## Complexity detail
The query must emit $R=PQ$ rows and account for all $E$ attendance rows. With indexed or hash-assisted matching, the logical work is $O(R+E)$. The generated pair domain, aggregation state, and result can occupy $O(R+E)$ space, depending on the physical database plan.

## Alternatives and edge cases
- **Start from `Examinations`:** It omits every zero-attendance student-subject pair.
- **Correlated count subquery:** It is concise but may rescan `Examinations` once for each of the $R$ pairs, requiring $O(RE)$ work.
- **Count `*` after the left join:** It incorrectly reports `1` for a pair with no examination because the preserved outer row is counted.
- **Duplicate attendance rows:** Each represents a separate exam attendance and must increase the count.
- **Student with no exams:** The student still appears once for every subject, all with zero counts.
- **Required order:** Both `student_id` and `subject_name` must participate in the final ascending order.
