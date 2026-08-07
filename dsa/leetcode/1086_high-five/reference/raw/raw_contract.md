## Function Contract

**Input**

- `items`: an array of pairs `[student_id, score]`.

Let $N$ be the number of score records and $S$ the number of distinct student identifiers. Every represented student has at least five records, and repeated score values are separate records.

**Return value**

- One row `[student_id, average]` for every distinct student.
- `average` is the integer quotient obtained by summing that student's five highest scores and dividing by `5`.
- Rows are ordered by `student_id` in increasing order.
