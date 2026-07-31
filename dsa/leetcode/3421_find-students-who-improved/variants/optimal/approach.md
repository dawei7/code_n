## General

First reduce each `(student_id, subject)` group to its chronological endpoints. `MIN(exam_date)` is the first exam date and `MAX(exam_date)` is the latest. Requiring at least two rows excludes groups that have no meaningful before-and-after comparison; the composite primary key guarantees that the two dates identify exactly one row each within a group.

Join the grouped endpoint dates back to `Scores` twice. The first join retrieves the score attached to the earliest date, and the second retrieves the score attached to the latest date. This distinction is essential: `MIN(score)` and `MAX(score)` would measure score extrema, which may occur on intermediate exams and say nothing about chronological improvement.

Filter with `latest_score > first_score`, so equal scores and declines are excluded. The joins produce one row per eligible group, and the final two-column ordering implements the required deterministic result order.

## Complexity detail

Let $r$ be the number of score rows and $g$ the number of student-subject groups. A conservative engine-independent bound for grouping and final ordering is $O(r\log r)$ time and $O(r)$ auxiliary space. With the composite primary-key index, the two endpoint joins use keyed lookups; database optimizers may achieve better constants or near-linear scans, but the manifest records the conservative bound.

The benchmark defines `size` as $r$ and uses 32, 128, and 256 chronologically distinct exams in one group, spanning 8x. The accepted grouped query scans and aggregates those rows before two keyed joins. A correct baseline that materializes every ordered pair of exams in the group creates $\Theta(r^2)$ rows and must fail only the scaling verdict.

## Alternatives and edge cases

- **Compare `MIN(score)` with `MAX(score)`:** These scores can belong to intermediate dates and can falsely report improvement when the latest score declined.
- **Use `LAG` on every exam:** Window functions can work, but comparing only the final row with its immediate predecessor does not compare the latest score with the first score.
- **Self-join every earlier and later exam:** This generates many irrelevant pairs and can become quadratic before reducing back to the endpoints.
- **One exam in a group:** It has no distinct first/latest comparison and must be omitted.
- **Equal endpoint scores:** Improvement is strict, so equality does not qualify.
- **Intermediate high or low scores:** Only the chronological first and latest rows affect the result.
- **Several subjects for one student:** Each subject forms an independent group.
- **Output ordering:** Sort numerically by `student_id`, then lexicographically by `subject`, regardless of insertion order.
