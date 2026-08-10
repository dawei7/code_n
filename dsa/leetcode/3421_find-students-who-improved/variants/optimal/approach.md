## General

**Compare chronological endpoints within each student-subject history.** Improvement is not based on the minimum and maximum scores, nor on any pair of consecutive exams. For every distinct `(student_id, subject)` group, the query must identify the score on the earliest date and the score on the latest date, then keep the group only when the latter is strictly larger.

The first common table expression, `RankedScores`, keeps every row from `Scores` and adds two independent row numbers.

`rn_first` is computed with

`PARTITION BY student_id, subject ORDER BY exam_date ASC`.

Partitioning restarts numbering for each student's separate subject. Ascending date order gives row number one to that group's earliest exam.

`rn_latest` uses the same partition but orders `exam_date DESC`. It gives row number one to the latest exam.

The primary key is `(student_id, subject, exam_date)`, so one student cannot have two rows for the same subject on the same exam date. Consequently, each partition has exactly one first-ranked row and exactly one latest-ranked row; no tie-breaking column is needed.

The declared date column is text, but the represented dates use the sortable `YYYY-MM-DD` form shown in the data model and example. Lexicographic ascending and descending order then agree with chronological order.

**Join the two endpoint rows from the ranked data.** The second CTE, `FirstAndLatestScores`, refers to `RankedScores` twice:

- alias `f` supplies the row with `f.rn_first = 1`;
- alias `l` supplies the row with `l.rn_latest = 1`.

They are joined on both `student_id` and `subject`. Joining on student alone would incorrectly compare a first score from one subject with a latest score from another. For each group, the selected columns become `first_score` from `f.score` and `latest_score` from `l.score`.

Although the join condition itself could pair many rows within a group, the two row-number filters leave exactly one endpoint row on each side. The result therefore has at most one output candidate per student-subject pair.

**Why groups with only one exam disappear.** In a one-row partition, that same row has both `rn_first = 1` and `rn_latest = 1`. The self-join produces a candidate whose `first_score` equals `latest_score`. The final condition `latest_score > first_score` is false, so the group is excluded. This automatically enforces the “at least two different dates” requirement without a separate `COUNT(*) >= 2` test.

For a group with multiple dates, the primary key guarantees the first and latest rows are different. The strict greater-than filter keeps genuine improvement, excludes equal scores, and excludes declines.

**Produce the requested rows and order.** The outer query selects all four columns from `FirstAndLatestScores`:

`student_id`, `subject`, `first_score`, and `latest_score`.

It filters to strict improvements and uses `ORDER BY 1, 2`. Positional expression `1` is `student_id` and expression `2` is `subject`. Ascending is SQL's default, so results are ordered by student ID first and subject second, both ascending.

For student $101$ in Math, the ascending rank selects score $70$ on the January date, and the descending rank selects $85$ on the February date. The final comparison succeeds. For the same student's Physics group, $60$ is not greater than $65$, so it is removed. Student $103$ has one Math row, which joins to itself and then fails the strict comparison.

**Why this is correct.** Window functions assign each row its exact chronological position inside the correct group. The filters select the unique earliest and latest rows, and the join keeps those rows paired only with their shared student and subject. The final predicate is exactly the definition of score improvement. Therefore, every returned row satisfies both eligibility conditions.

Conversely, any student-subject group with at least two exams and a higher latest score has one earliest row marked `rn_first = 1` and one latest row marked `rn_latest = 1`. Their join candidate passes the comparison and is returned. No qualifying group can be omitted.

The two rankings are both needed. A single ascending row number identifies the first row, but finding the last row would then require knowing the partition count or using a separate window expression such as `LAST_VALUE` with an explicitly correct frame. Paired row numbers keep the endpoint selection clear.

## Complexity detail

Let $r$ be the number of rows in `Scores`. Computing each partitioned row number generally requires ordering rows by the partition keys and exam date. In a straightforward plan, window sorting costs $O(r\log r)$ time and $O(r)$ working or materialization space. Both window expressions share compatible partition keys and opposite date direction; the exact number of physical sorts depends on the MySQL optimizer.

Joining endpoint rows and filtering are linear or near-linear with appropriate materialization/hash/index strategies, and final output ordering costs $O(q\log q)$ for $q\le r$ qualifying groups. The overall safe bound remains $O(r\log r)$ time and $O(r)$ space, matching the manifest. Database indexes and execution plans can lower constants or avoid some explicit sorts.

## Alternatives and edge cases

- **Aggregate minimum and maximum score:** `MIN(score)` and `MAX(score)` do not identify scores on the first and latest dates. A student could peak in the middle and later decline.
- **Aggregate endpoint dates then join:** Finding `MIN(exam_date)` and `MAX(exam_date)` per group and joining those dates back to `Scores` is also correct, but requires additional grouped and keyed joins.
- **`FIRST_VALUE` and `LAST_VALUE`:** Window endpoint functions can solve the problem, but `LAST_VALUE` is easy to misuse because its default frame often ends at the current row rather than the partition's final row.
- **Only one exam:** The row receives both endpoint ranks but fails strict improvement, correctly excluding it.
- **Equal first and latest scores:** Equality is not improvement, so `>` rather than `>=` is required.
- **Intermediate scores:** They do not affect qualification. Only the earliest and latest chronological scores matter.
- **Several subjects:** Partitioning by both columns prevents one subject's dates or scores from influencing another.
- **Unique dates:** The composite primary key removes endpoint ties within a group. Without that guarantee, an additional deterministic tie rule would be required.
- **Date text format:** Chronological correctness assumes a lexicographically sortable date representation such as `YYYY-MM-DD`. Arbitrary localized date strings should be converted to a date type before ordering.
- **Output ordering:** `ORDER BY 1, 2` is correct but positional. Naming `student_id, subject` explicitly would be more resistant to future select-list reordering.
