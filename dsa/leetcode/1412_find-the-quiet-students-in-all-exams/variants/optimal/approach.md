## General

**Turn “never highest or lowest” into per-exam ranks**

A student qualifies only if two conditions both hold:

1. The student took at least one exam.
2. Across every exam they took, their score was neither a lowest score nor a highest score.

The word “every” makes this easier to solve by first marking violations on individual Exam rows and then grouping those rows by student. If the grouped student has zero lowest-score violations and zero highest-score violations, every participation was quiet.

The common table expression `T` creates those row-level markers through two window ranks:

```sql
RANK() OVER (
    PARTITION BY exam_id
    ORDER BY score
) AS rk1
```

and

```sql
RANK() OVER (
    PARTITION BY exam_id
    ORDER BY score DESC
) AS rk2
```

`PARTITION BY exam_id` restarts each ranking for each exam. Scores from exam 10 must never be compared with scores from exam 20, even if the numerical values overlap.

**Why two directions are needed**

For `rk1`, ascending order puts the smallest score first, so `rk1 = 1` means the row holds a lowest score in that exam. For `rk2`, descending order puts the largest score first, so `rk2 = 1` means the row holds a highest score.

These are independent conditions. A middle score has both ranks greater than one. A minimum but nonmaximum score has `rk1 = 1` only. A maximum but nonminimum score has `rk2 = 1` only. In a one-participant exam, the same score is both minimum and maximum, so both ranks are one.

Using `RANK` rather than `ROW_NUMBER` is essential for ties. If three students share the lowest score, all three receive ascending rank one and all three must be disqualified. `ROW_NUMBER` would arbitrarily assign only one of them position one and could falsely treat the other tied students as quiet. The same reasoning applies to tied maximum scores.

The CTE retains `student_id` along with both ranks. It does not need `exam_id` in its output because the window computation has already encoded whether that particular participation was extreme.

**Why joining from `T` excludes nonparticipants**

The main query uses:

```sql
T
JOIN Student USING (student_id)
```

`T` contains one row for every Exam participation and no row for a student who never took an exam. Because this is an inner join, only identifiers present in `T` can reach the result. The contract's “took at least one exam” requirement is therefore satisfied automatically.

`USING (student_id)` is shorthand for equality between the same-named identifier columns. It also exposes a single merged `student_id` column, which makes the later selection concise. The join obtains `student_name` from the Student table.

**Collapse all participations to one decision per student**

`GROUP BY 1` groups by the first selected expression, `student_id`. Every T row for the same student enters one group, no matter which exam produced it. Since Student.`student_id` is unique, `student_name` is functionally determined by that identifier.

The `HAVING` clause examines aggregate properties of each complete group:

```sql
HAVING SUM(rk1 = 1) = 0 AND SUM(rk2 = 1) = 0
```

In MySQL, a true comparison contributes 1 and a false comparison contributes 0 to `SUM`. Therefore:

- `SUM(rk1 = 1)` counts how many exams placed this student at the minimum.
- `SUM(rk2 = 1)` counts how many exams placed this student at the maximum.

Both counts must be zero. One extreme result in even one exam makes the corresponding sum positive and removes the entire student group. This exactly captures “quiet in all exams,” not merely “quiet in at least one exam.”

The use of `HAVING` rather than `WHERE` is necessary because the decision depends on sums across the group. `WHERE` filters individual rows before grouping and cannot directly express the aggregate all-exams condition.

**Following the sample student Jade**

Jade participates in exam 10 with score 80 and exam 40 with score 70. In exam 10, the scores are 70, 80, and 90, so Jade is neither extreme. In exam 40, the scores are 60, 70, and 80, so she is again neither extreme. Both of Jade's T rows have `rk1 > 1` and `rk2 > 1`. Her two Boolean sums are zero, so she survives.

Daniel has several participations, but at least one is a lowest or highest score. His group has a positive extreme count and fails. Will has no Exam row, so he never appears in `T` and the inner join excludes him even though he has never recorded an extreme score.

**Ordering and selected columns**

The query returns only `student_id` and `student_name`. `ORDER BY 1` sorts by the first selected column, which is student ID, in ascending order by default. The output is therefore deterministic and satisfies the stated ordering.

**Why the query is correct**

For every Exam row, the two ranks correctly identify all tied and untied minima and maxima within that exam. Grouping gathers exactly the rows for one participating student. The HAVING condition accepts the group precisely when none of its rows carries either extreme marker. The inner join supplies the name while ensuring at least one participation exists. Thus every returned student is quiet in every exam they took, and every qualifying participating student is returned.

## Complexity detail

Let $E$ be the number of Exam rows and $S$ the number of Student rows. Computing the two window rankings requires organizing rows by exam and score. A comparison-sort execution plan takes $O(E \log E)$ time in the general case. The join and per-student grouping scan or hash their inputs in expected $O(E+S)$ time, and the final sort of at most $S$ result groups is bounded by $O(S \log S)$.

The manifest summarizes the intended dominant work as $O(E \log E + S)$. Exact physical cost depends on database indexes, partition sizes, statistics, and the optimizer. The ranked CTE may retain $O(E)$ rows, while join and grouping structures can use up to $O(E+S)$ working space, matching the manifest's $O(E+S)$ bound.

## Alternatives and edge cases

- **Per-exam `MIN` and `MAX` subquery:** Compute both extremes for each exam, join them back to Exam, and reject students with a matching extreme. This is correct but requires another aggregation and join.
- **`NOT EXISTS` disqualifier:** Select participating students for whom no Exam row equals its exam's minimum or maximum. This can read naturally but may involve correlated work unless the optimizer rewrites it well.
- **Conditional aggregation without ranks:** Window `MIN(score)` and `MAX(score)` values can be attached to each row, followed by Boolean sums. It handles ties correctly and expresses the same idea.
- **`ROW_NUMBER`:** This is incorrect when scores tie because only one tied row gets number one. `RANK` marks every student at an extreme.
- **Student with no exams:** The inner join from `T` excludes the student, as required.
- **Only participant in an exam:** The student is both lowest and highest and must be disqualified.
- **All scores tied in an exam:** Every participant receives rank one in both directions, so none can be quiet across that exam.
- **Tie only at one extreme:** Every student sharing that minimum or maximum is disqualified, while strict middle scores remain eligible.
- **Quiet in one exam but extreme in another:** Group-level sums detect the single violation and exclude the student.
- **Ordinal syntax:** `GROUP BY 1` and `ORDER BY 1` refer to the first selected column. Naming `student_id` explicitly would be more self-documenting but is logically equivalent here.
