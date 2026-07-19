## General
**Join each school to feasible cutoffs**

Left join `Schools` to `Exam` using
`Exam.student_count <= Schools.capacity`. A matched row is a recorded cutoff
for which every potentially applying student fits. The left join is essential:
a school with no qualifying exam row must still appear in the result.

**Why the smallest feasible score is optimal**

Because the exam data is monotone, lowering a score can only keep or increase
the number of qualifying students. Therefore, among all feasible rows for one
school, the minimum score admits the greatest possible population. If several
scores have the same `student_count`, taking the minimum score also applies the
required tie rule directly.

Group by `school_id` and compute `MIN(Exam.score)`. When the left join found no
eligible row, that minimum is `NULL`; convert it to `-1` with `COALESCE`.

**Preserve one result for every school**

Grouping the rows produced by the left join yields exactly one output row per
unique school identifier. Every selected non-null score comes from `Exam` and
satisfies the capacity constraint, while the monotonic argument proves no
other recorded cutoff can allow more applicants.

## Complexity detail
Without a supporting index on `student_count`, the inequality join may compare
each of $S$ schools with all $E$ exam rows, taking $O(SE)$ time. Grouping keeps
one aggregate result per school, requiring $O(S)$ result or aggregation space.
Database engines may improve physical execution when additional indexes or
ordering are available, but the query does not assume them.

## Alternatives and edge cases
- **Correlated scalar subquery:** Select `MIN(score)` from eligible `Exam` rows
  separately for each school. This expresses the same $O(SE)$ logical work but
  may be less convenient for some optimizers.
- **Redundant Cartesian joins:** Joining additional copies of `Exam` does not
  change the answer when grouped carefully, but multiplies work unnecessarily.
- `MIN(score)` must be applied only after filtering by capacity; the globally
  smallest exam score may admit too many students.
- If a school's capacity is smaller than every `student_count`, its score is
  `-1`, not the highest known cutoff.
- If capacity supports every exam row, the globally smallest recorded score is
  selected.
- Equal `student_count` values at different scores are resolved by choosing the
  smaller score.
- Output ordering is not part of the contract.
