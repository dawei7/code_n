## General
**Mark both extremes inside each exam.** In a common table expression, assign each `Exam` row an ascending score rank and a descending score rank, partitioned by `exam_id`. A row with ascending rank one is tied for the minimum; a row with descending rank one is tied for the maximum. Ranking rather than numbering is essential because all equal extreme scores receive rank one.

**Require a clean complete history.** Group the ranked rows by `student_id`. A student qualifies only when the minimum ascending rank and minimum descending rank across all their rows are both greater than one. The group exists only for exam participants, so students with no exam rows are naturally excluded.

Join the qualifying IDs to `Student`, project the required identity columns, and order by `student_id`. Every excluded participant has at least one rank-one extreme row. Conversely, if neither minimum rank equals one, every score is strictly above its exam minimum and strictly below its exam maximum, which is exactly the quiet-student condition.

## Complexity detail
Let $E$ be the number of rows in `Exam` and $S$ the number of rows in `Student`. Partitioned ranking is bounded by $O(E \log E)$ time, while grouping, joining, and ordering the qualifying identities fit within $O(E + S)$ additional work under indexed identifiers and the stated bound. The ranked rows and grouped identities use $O(E + S)$ working space.

## Alternatives and edge cases
- **Per-exam extrema then anti-join:** Aggregate each exam's minimum and maximum once, mark students matching either value, and exclude those IDs. This has comparable complexity and can be clearer on systems without window functions.
- **Correlated minimum and maximum:** Recompute both extrema for every participation row. It is correct but can rescan `Exam` repeatedly and degrade toward $O(E^2)$.
- **Tied extremes:** `RANK`, not `ROW_NUMBER`, ensures every student sharing a minimum or maximum is disqualified.
- **Single-participant exam:** The sole score is both minimum and maximum, so that student is not quiet.
- **Multiple exams:** One extreme result anywhere disqualifies an otherwise middle-scoring student.
- **No participation:** A student absent from `Exam` must not appear.
- **Output order:** Sort by numeric `student_id`, regardless of student name.
