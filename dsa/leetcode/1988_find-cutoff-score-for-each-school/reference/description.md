## Description

The `Schools` table gives each school's unique identifier and maximum student
capacity. The `Exam` table associates an available cutoff `score` with
`student_count`, the number of students who earned at least that score. Exam
data is monotone: a higher cutoff never has more qualifying students than a
lower cutoff.

For every school, choose a cutoff that appears in `Exam`. All students meeting
it must fit within the school's capacity, and the school wants as many students
as possible to remain eligible. If several cutoffs allow that same maximum
population, use the smallest score. Report `-1` when no recorded cutoff has a
qualifying population within capacity. Return one row per school in any order.
