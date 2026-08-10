## General

**Translate capacity into a join condition**

An `Exam` row says that `student_count` students earned at least its `score`. If a school uses that score as its cutoff, every one of those students might apply. The cutoff is safe exactly when

`school.capacity >= exam.student_count`.

The query places this condition directly in the join between `Schools` and `Exam`. For each school, the matching exam rows are precisely the score thresholds whose possible applicant count does not exceed capacity.

**Why a left join is required**

Some school may be too small even for the highest recorded cutoff. Such a school has no feasible `Exam` row, but it must still appear in the result with score -1.

An inner join would discard it completely. `LEFT JOIN` instead retains one synthetic row for the school and fills the exam-side columns with SQL `NULL` when no score matches. This preserves every `school_id` for grouping and fallback handling.

**Choose the smallest feasible score**

The exam data is monotone: as score increases, `student_count` cannot increase. Once a threshold is feasible, higher thresholds are also no more demanding, although they may allow fewer students to apply.

Schools first want to maximize the number of possible applicants. Lowering the cutoff can only keep or increase that number, so the lowest feasible score is an optimal choice. If several scores have the same student count, the explicit tie rule also chooses the smallest score. Thus `MIN(score)` over all feasible joined rows implements both priorities.

For capacity 99 in the example, scores 975, 966, 844, and 749 are feasible, while 744 would allow 100 students and is not. The minimum feasible score is 749.

**Produce -1 when no score is known to be safe**

The exact select expression is

`MIN(COALESCE(score, -1)) AS score`.

For a school with matches, left join produces its real matching rows and their nonnull scores; there is no additional unmatched row. `COALESCE` leaves those scores unchanged, and `MIN` chooses the smallest.

For a school with no match, its single preserved row has null `score`. `COALESCE` converts that null to -1, and the minimum is therefore -1.

Putting `COALESCE` outside the aggregate, as `COALESCE(MIN(score), -1)`, would express the intention more directly and has the same result under this schema. The exact source uses it inside.

**Group once per school**

The join can produce many feasible rows for one school. `GROUP BY school_id` collapses them to one output row and gives `MIN` the correct per-school scope.

`school_id` is unique in `Schools`, so every group refers to one capacity. The result order is unspecified because the contract permits any order.

**Why this query is correct**

For a school with at least one feasible score, the join includes all and only exam rows whose student count fits its capacity. Monotonic exam semantics ensure that the minimum score among these rows admits the largest possible population represented by the table; choosing the smallest score also resolves equal-count ties correctly.

For a school without a feasible row, no score in the available exam data guarantees that all qualifying students fit. The left-join fallback reports -1 as required.

Every school is preserved by the left join and grouped separately, so the query produces exactly one correct row per school.

**Why the smallest score is not merely an arbitrary minimum**

It can seem that maximizing students should use `MAX(student_count)` first. Because the data is logically consistent, sorting scores downward sorts counts nondecreasingly in the opposite direction. Among capacity-safe rows, moving to a smaller score never reduces the possible applicant count. The minimum-score choice therefore already reaches the maximum count. If the count stays flat across several thresholds, the same move selects the requested smallest score.

This reasoning depends on the stated monotonic guarantee. Without it, minimum feasible score and maximum feasible student count could conflict and a two-stage ranking would be necessary.

## Complexity detail

Let $S$ be the number of schools and $E$ the number of exam rows. Logically, the inequality join may test up to $SE$ school-score pairs, so the manifest's $O(SE)$ time is an appropriate worst-case query-level bound.

Aggregation keeps one result state per school, using $O(S)$ logical space. A database may use indexes, sorting, hashing, or temporary storage, so physical costs depend on the execution plan. The output itself has $S$ rows.

## Alternatives and edge cases

- **Correlated subquery:** Select `MIN(score)` from `Exam` under each school's capacity and coalesce null to -1; this states the per-school search directly.
- **Cross join then filter:** Correct but materializes or reasons about all $SE$ pairs before filtering.
- **Rank by student count then score:** More general if monotonicity were absent, but unnecessary under the guaranteed ordering relationship.
- **Inner join:** Incorrectly removes schools that have no feasible score.
- **No feasible exam row:** The synthetic null row becomes -1.
- **Every exam row feasible:** The smallest score in the table is selected.
- **Capacity exactly equals student count:** It is feasible because the join uses `>=`.
- **Equal student counts at different scores:** The smallest feasible score satisfies the tie rule.
- **Unique school IDs:** Ensure one capacity and one aggregate group per school.
- **Unique score values:** Prevent duplicate threshold rows in `Exam`.
- **Monotone exam data:** Makes minimum feasible score consistent with maximizing possible applicants.
- **Any output order:** No `ORDER BY` is required.
- **No table mutation:** The query only joins and aggregates existing rows.
