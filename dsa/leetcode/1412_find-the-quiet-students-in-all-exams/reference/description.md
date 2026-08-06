## Description

A quiet student has participated in at least one exam and has never earned either the highest score or the lowest score in any exam they took. The comparison is exam-local: a score is evaluated only against the other scores carrying the same `exam_id`. When several students share an extreme score, each of them earned that highest or lowest value and is therefore disqualified.

Report the ID and name of every student who is quiet across their complete exam history. A student with no `Exam` row must not appear. Order the result by `student_id`.
