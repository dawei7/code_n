## General

**Construct each student's required course roster.** Join every student to the courses whose `major` matches the student's major. Each resulting row represents one obligation: that student must have an `A` enrollment for that course. The inner join intentionally excludes students whose major has no offered courses rather than treating an empty course set as automatically complete.

**Attach only successful attempts.** Left join `enrollments` by both `student_id` and `course_id`, with `grade = 'A'` inside the join condition. Keeping this filter in the join preserves a required-course row when no A attempt exists; its enrollment columns are then `NULL`. Filtering in a `WHERE` clause would discard the missing obligation and could make an incomplete student appear complete.

**Compare required and completed courses.** Group by student. `COUNT(DISTINCT c.course_id)` counts the courses that the student's major requires, while `COUNT(DISTINCT e.course_id)` counts those required courses for which the student has at least one A attempt. The student qualifies exactly when the two counts match. Distinct course identifiers prevent repeated A semesters from inflating the completed count.

Every returned student has a matched A enrollment for as many distinct major courses as the roster contains, and the enrollment join cannot match a course outside that roster; therefore every required course is covered. Conversely, a student with an A in every major course contributes each required course to both distinct counts and passes the `HAVING` test. Sorting by `student_id` supplies the requested order.

## Complexity detail

Let $s$, $c$, and $e$ be the table sizes and $r = s + c + e$. With ordinary indexes or hash-assisted equality joins, the database processes the matched roster and enrollment rows in $O(r)$ work for legal input records, while grouping, distinct aggregation, and final ordering give $O(r\log r)$ worst-case time. The joins, group state, distinct sets, and sort can require $O(r)$ auxiliary database storage.

The app-local SQLite query and the remotely verified MySQL query use the same standard joins and aggregates.

## Alternatives and edge cases

- **Double `NOT EXISTS`:** Reject a student when some course in the student's major lacks an A enrollment. This expresses relational division directly, but a plan that repeatedly scans the tables may be slower than indexed joins and aggregation.
- **Count every enrollment row:** Comparing raw row counts is incorrect because retaking one course can produce several enrollment rows without covering another required course.
- **Filter A grades after the left join:** A `WHERE e.grade = 'A'` predicate removes unmatched required courses and destroys the evidence that a student is missing one.
- **Non-A attempts:** A B, C, or other grade does not cover a required course.
- **Retakes:** At least one A attempt covers that course; additional A or non-A semesters do not change the distinct-course result.
- **Courses outside the major:** They neither help nor hurt qualification because they are absent from the student's required roster.
- **No offered courses:** The inner student-to-course join excludes a student whose major has no course to complete.
- **Output ordering:** Grouped output has no guaranteed order, so `ORDER BY student_id` remains necessary.

