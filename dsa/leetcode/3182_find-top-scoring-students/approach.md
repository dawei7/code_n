## General

**Create one required row per student-course pair**

`students JOIN courses USING (major)` pairs every student with every course offered by that student's major.

This turns the universal requirement “all major courses” into rows that can be checked by aggregation. A student with two required courses receives two base rows.

The left join to `enrollments` uses both `student_id` and `course_id`. A completed enrollment attaches its grade. A missing course enrollment keeps the required row but supplies null enrollment columns, which is why a left join is necessary.

**Compare A rows with all required joined rows**

MySQL expression `grade = 'A'` evaluates to 1 for A, 0 for another non-null grade, and null for missing enrollment.

`SUM(grade = 'A')` counts A enrollment rows. `COUNT(major)` counts every joined row because `major` comes from required student/course data and is non-null.

Equality holds only when every counted row contributes one—meaning every required joined record has grade A and none is missing or non-A.

Grouping by `student_id` makes this test independent per student. `ORDER BY 1` returns passing IDs ascending.

**Example**

For a major with courses 101 and 102:

- grades A and A yield sum 2 and count 2, so student passes;
- grades A and B yield 1 versus 2, so fails;
- enrollment only in 101 with A leaves course 102 null, yielding sum 1 versus count 2, so fails.

**Repeated enrollment-semester behavior**

The enrollment primary key includes semester, so a student may have several rows for the same course across semesters. The join then produces several rows for that required course.

The exact query requires every joined attempt to have grade A. Two A attempts count 2 equals two joined rows and pass. An A and a B produce 1 versus 2 and fail.

The prose could alternatively be interpreted as “has achieved an A in each course at least once,” in which case a later A retake should qualify despite an earlier B. The exact query does not implement that interpretation. It implements “all enrollment records for every required course are A,” plus no missing course.

**Students whose major has no course**

The first join is inner. A student in a major absent from `courses` creates no group and is not returned. This treats “taken all courses” as requiring at least one offered course rather than vacuous truth.


For each student, joined rows enumerate every required course and every matching enrollment attempt, with a null row for a completely missing course. Equality in `HAVING` is possible precisely when all produced rows are A.

Therefore, under the interpretation that all attempts must be A, every returned student satisfies the requirement and every such student is returned.

**Null aggregation detail**

If some rows are A and one is missing, `SUM` ignores the null but `COUNT(major)` includes its required row, so equality fails. If all grades are missing, `SUM` can be null and comparison to a positive count is not true, also failing.

**Why COUNT uses major**

Counting `grade` would be wrong because a missing enrollment has null grade and would disappear from both sides, potentially making an incomplete student pass. Counting non-null `major` deliberately retains every required joined row in the denominator.

The query does not count distinct course IDs. That is acceptable only for its “every joined attempt is A” semantics; a distinct-course interpretation requires separate aggregation per course.

## Complexity detail

Let $r$ be total joined-row volume across required courses and enrollment attempts.

Joins and grouping are typically $O(r)$ with hashing or $O(r\log r)$ with sorting/index operations. Final ordering by passing students can add $O(s\log s)$. The manifest's conservative $O(r\log r)$ time and $O(r)$ intermediate space are reasonable.

Actual SQL cost depends on indexes for major and composite join keys.

Output is at most one row per grouped student.

## Alternatives and edge cases

- **Double NOT EXISTS:** Select a student for whom no required course lacks an A. This expresses universal logic directly.
- **Count distinct required courses:** Compare major course count with distinct courses having at least one A; this supports the “ever achieved A” interpretation.
- **Inner join enrollments:** Incorrect for detecting missing courses because absent rows disappear instead of causing failure.
- **Missing required course:** Left-join null makes the student fail.
- **One B attempt:** Exact query fails even if another semester has A.
- **Several A attempts:** They duplicate numerator and denominator equally and still pass.
- **Major with no courses:** Student disappears in the initial inner join.
- **Student not enrolled anywhere:** Required rows remain with null grades and fail.
- **Course IDs globally unique:** The enrollment join uses student and course and does not need major again.
- **Boolean SUM:** Relies on MySQL treating true as 1 and false as 0.
- **Null grade:** It cannot contribute an A and prevents equality through the counted required row.
- **Final ordering:** Positional `ORDER BY 1` sorts student IDs.
