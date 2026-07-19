## General
**Define the complete preference order:** Within one student's rows, a larger `grade` is always better. When grades are equal, a smaller `course_id` is better. These two keys create a deterministic order because the composite primary key prevents duplicate courses for a student.

**Rank independently inside each student:** Use `ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY grade DESC, course_id ASC)`. Partitioning prevents grades from different students from competing. The first row in every partition is exactly the highest grade with the required smallest-course tie-break.

**Select one winner and impose the requested result order:** Filter the ranked relation to `row_number = 1`, project the three required columns, and order by `student_id`. Every returned row dominates or ties-and-precedes every other course for its student. Conversely, each nonempty student partition has exactly one first row, so every student appears exactly once.

## Complexity detail
A conventional window plan sorts the $R$ rows by partition and preference keys in $O(R \log R)$ time and can use $O(R)$ execution space. Existing indexes or an engine-specific top-per-group optimization may improve the physical plan, but the stated bound does not assume either.

## Alternatives and edge cases
- **Aggregate then join:** Find each student's maximum grade, join those rows back, and apply `MIN(course_id)` to ties. It is correct but requires multiple grouping stages.
- **Correlated anti-dominance query:** Keep a row only when no better row exists for the same student. It states the rule directly but can take $O(R^2)$ time without a supporting index.
- **`RANK` by grade alone:** It can return several rows when the maximum grade is tied and therefore misses the smallest-course rule.
- **One enrollment:** That sole row is necessarily the student's result.
- **Tied highest grades:** The ascending secondary key selects the smallest course identifier.
- **Lower-grade smaller course:** Grade has priority, so a smaller `course_id` cannot defeat a strictly higher grade.
- **Input order:** Window ordering, not row arrival order, determines the winner.
- **Result order:** The final `ORDER BY student_id` is required independently of the ranking inside partitions.
