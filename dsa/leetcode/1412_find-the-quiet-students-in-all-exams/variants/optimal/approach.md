## General

**Mark every exam-local extreme.** For each `Exam` row, compute two window ranks partitioned by `exam_id`: `low_rank` orders `score` ascending and `high_rank` orders it descending. An ascending rank of one means the row's score equals that exam's minimum; a descending rank of one means it equals the maximum. `RANK` is essential here because every row tied at an extreme receives rank one. `ROW_NUMBER` would mark only one arbitrary member of a tie and could incorrectly admit the others.

**Reduce the complete student history.** Group the ranked rows by `student_id`. The condition `MIN(low_rank) > 1` proves that none of the student's rows is a minimum, and `MIN(high_rank) > 1` proves that none is a maximum. Both must hold: a single rank-one row in either direction makes the corresponding minimum equal one and rejects the entire history. Because groups are formed from `Exam`, students without participation never become candidates.

**Recover the requested identity.** Join each qualifying ID to `Student`, project the source ID and name, and sort by `student_id`. Every emitted student participated and had no extreme row. Conversely, every participating student who was never extreme has both ranks above one on every row, so both grouped minima exceed one and that student is emitted. This proves the filter exactly matches the quiet-student definition.

## Complexity detail

Let $E$ be the number of `Exam` rows and $S$ the number of `Student` rows. Sorting the exam partitions for the two window rankings takes $O(E \log E)$ time in the general comparison-based database model. Grouping, joining, and emitting the ordered result fit within the branch's $O(E \log E + S)$ bound. The ranked relation, partition state, and grouped student IDs require $O(E + S)$ working space.

## Alternatives and edge cases

- **Per-exam extrema plus anti-join:** Compute each exam's `MIN(score)` and `MAX(score)`, collect every student matching either value, and subtract those IDs from participants. It is correct with comparable complexity but needs more intermediate relations.
- **Correlated extrema:** Recompute an exam's minimum and maximum for every participation row. This is correct but can repeatedly scan `Exam` and degrade toward $O(E^2)$ without supporting indexes.
- **`ROW_NUMBER` instead of `RANK`:** This is incorrect when an extreme score is tied because only one tied row receives row number one.
- **Tied minimum or maximum:** Every student sharing the extreme value is disqualified; middle scores in the same exam may still qualify.
- **All scores equal:** Every participant is simultaneously tied for the minimum and maximum, so none is quiet.
- **Single-participant exam:** The only score is both extremes and disqualifies that student.
- **Several exams:** One extreme result anywhere rejects the student even when all other scores are strictly internal.
- **No participation:** A student absent from `Exam` has no qualifying history and must not appear.
- **Duplicate names:** Windowing, grouping, and joining use student IDs, so equal names cannot merge different students.
- **Output order:** Sort by numeric `student_id` as required, independent of student or exam input order.
