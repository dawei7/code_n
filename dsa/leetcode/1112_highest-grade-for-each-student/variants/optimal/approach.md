## General

**Define one complete priority order per student**

For each student, the desired row is determined by two priorities. A larger grade is always better. When grades tie, a smaller course ID is better.

The window ordering writes these rules directly:

`ORDER BY grade DESC, course_id`

`DESC` puts the maximum grade first. Course ID uses ascending order by default, so the smallest tied course comes first.

**Rank rows without collapsing their columns**

A grouped `MAX(grade)` could find the best grade, but it would not by itself identify which course should be returned. The query needs the complete enrollment row after applying both priorities.

`RANK() OVER (PARTITION BY student_id ... )` keeps every original row and adds its position within that student’s ordered enrollments. `PARTITION BY student_id` restarts ranking for each student, preventing one student’s grades from affecting another’s selection.

The best row in every partition receives `rk = 1`. The outer query filters to those rows and selects the original `student_id`, `course_id`, and `grade`.

**Why rank one is unique here**

`RANK` normally gives the same rank to rows tied on every ordering expression. In this query, a tie would require equal grade and equal course ID for the same student.

The composite primary key `(student_id, course_id)` forbids two rows with the same student and course. Therefore, no two rows within one partition can tie on both ordering expressions. Exactly one row receives rank one for each represented student.

This is why `RANK`, `ROW_NUMBER`, and `DENSE_RANK` would all select the same single winner under the source constraints, although their behavior differs for true ordering ties.

**Walk through a tied grade**

Suppose student two has grade 95 in courses two and three. Both rows tie on the first ordering key. The second key orders course two before course three, so course two receives rank one and is returned.

If course three instead had grade 96, grade ordering would dominate course ID. Course three would rank first despite its larger ID, because the tie-breaker is consulted only when maximum grades are equal.

**Produce the required global order**

Window ranking orders rows only inside partitions for ranking purposes; it does not guarantee final output order. The outer `ORDER BY student_id` explicitly sorts the selected winners by student ID ascending, as required.

If `Enrollments` is empty, the CTE has no rows, the rank filter selects nothing, and the result is the correct empty table.

The outer sort is applied after one winner has been chosen per student. It therefore orders only the result rows and cannot change which course won inside any student's partition.

**Why the result is correct**

Inside each student partition, descending grade ensures that no row with a smaller grade can precede a maximum-grade row. Among maximum-grade rows, ascending course ID places the smallest course first. The primary key makes that first row unique, and filtering rank one keeps it.

Partitions cover every represented student independently, so exactly one correct row is returned per student. The final sort supplies the requested presentation order.

## Complexity detail

Let $R$ be the number of enrollment rows. A typical database plan sorts rows by student ID, descending grade, and course ID to evaluate the window. General comparison sorting costs $O(R\log R)$ time.

The window stage and sort may materialize $O(R)$ rows or keys, giving the manifest’s $O(R)$ space bound. The filtered output contains at most $R$ rows, one per student.

Indexes matching the partition and ordering columns can reduce sorting work in practice, and an optimizer may choose other physical operations. The SQL describes a logical result rather than forcing one execution algorithm.

## Alternatives and edge cases

- **`ROW_NUMBER`:** Assign row numbers with the same partition and ordering, then keep one. It communicates the one-winner intent directly and is equivalent under the composite primary key.
- **Maximum-grade CTE plus join:** Find `MAX(grade)` per student, join back to matching rows, then take the minimum course ID among ties. This works but needs multiple logical stages.
- **Correlated subquery:** Reject a row when a better grade or equal grade with smaller course exists. It expresses dominance directly but is usually harder to read and optimize.
- **Group only by student with arbitrary course:** Incorrect because SQL cannot safely associate an unaggregated course ID with the maximum grade.
- **One enrollment:** That row is rank one and is returned.
- **Several equal maximum grades:** The smallest course ID wins through the second ordering key.
- **Smaller course with lower grade:** It does not win because grade has higher priority.
- **Negative or null grades:** Null is explicitly forbidden; numeric grade ordering is therefore unambiguous.
- **Duplicate student-course row:** The primary key forbids it, which guarantees a unique complete ordering.
- **Students with different enrollment counts:** Partitioning handles each independently, including students with only one course.
- **Final ordering:** The outer `ORDER BY` is necessary because window ordering alone does not promise result-table order.
- **Empty table:** No partitions or winner rows are created.
