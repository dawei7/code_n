## General

**Count each major's mandatory roster.** The first common table expression groups mandatory courses by `major`. This produces the exact number of distinct course obligations that a student in each major must cover. A missing row means that the major has no mandatory courses, so the later comparison uses zero through `COALESCE`.

**Aggregate every enrollment once per student.** Join `students` to all of their `enrollments`, then attach the matching `courses` row by `course_id`. Keeping enrollments outside the student's major is essential because every enrollment contributes to `AVG(GPA)`.

Conditional distinct counts isolate the two major-specific grade requirements. A course contributes to `passed_mandatory` only when it belongs to the student's major, is mandatory, and has an `A` attempt. A course contributes to `passed_electives` only when it belongs to the major, is non-mandatory, and has an `A` or `B` attempt. `COUNT(DISTINCT course_id)` prevents retakes from replacing a different required or elective course.

**Apply the three independent gates.** Retain a student only when the qualifying mandatory count equals the complete mandatory roster, the qualifying elective count is at least two, and the average over all enrollment GPA values is at least 2.5. Finally, sort the surviving identifiers.

Every returned student covers every mandatory course because the qualifying distinct count equals the full roster and can contain only courses from that roster. The elective count certifies two distinct acceptable major electives, and the unfiltered enrollment average certifies the global GPA requirement. Conversely, any student satisfying the contract contributes every required course, at least two electives, and an adequate average to these aggregates, so all three predicates accept that student.

## Complexity detail

Let $r=s+c+e$ be the total number of input rows. With ordinary indexes or hash-assisted equality joins, the joins and grouped scans are linear in their processed rows; grouping, distinct aggregation, and final ordering give $O(r\log r)$ worst-case time. The major counts, joined rows, distinct sets, group state, and sort may require $O(r)$ auxiliary database storage.

The app-local SQLite query and the remotely verified MySQL query use the same standard CTEs, joins, conditional aggregates, and predicates.

## Alternatives and edge cases

- **Three independent qualifying-student CTEs:** Intersecting separate mandatory, elective, and GPA result sets is valid, but it scans and groups the enrollment data repeatedly.
- **Correlated `NOT EXISTS`:** Relational division can verify mandatory coverage directly, though an unfavorable plan may rescan the course or enrollment table for every student.
- **Raw enrollment counts:** Counting rows instead of distinct course IDs is incorrect because repeated semesters for one course cannot replace a missing course.
- **Outside-major courses:** They never satisfy mandatory or elective counts, but their GPA values must remain in the overall average.
- **Retakes:** One qualifying attempt covers a course once; all attempts, including lower-grade attempts, still affect average GPA.
- **No mandatory courses:** The required count is zero, so a student can still qualify by meeting the elective and GPA requirements.
- **Fewer than two electives:** Even perfect mandatory grades and GPA do not qualify the student.
- **Grade and GPA independence:** Use the letter grade for course requirements and the numeric `GPA` column for the average; neither can be inferred from the other.
- **Exact GPA boundary:** An average of exactly 2.5 qualifies.
- **No enrollments:** The average is `NULL`, so the student cannot pass all criteria.
- **Output ordering:** Aggregation does not guarantee order; `ORDER BY student_id` is required.
