# Find Cutoff Score for Each School

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1988 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/find-cutoff-score-for-each-school/) |

## Problem Description
### Goal
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

### Function Contract
**Inputs**

- `Schools(school_id, capacity)`: one row per school; `school_id` is unique and
  `capacity` is the maximum number of accepted students.
- `Exam(score, student_count)`: one row per available score; `score` is unique,
  and `student_count` is the number of students scoring at least that value.
- Let $S$ and $E$ be the numbers of rows in `Schools` and `Exam`.

**Return value**

- A table with columns `school_id` and `score`, containing each school and its
  chosen minimum cutoff, or `-1` when no exam row satisfies
  `student_count <= capacity`.
- Result-row order is irrelevant.

### Examples
**Example 1**

`Schools`

| school_id | capacity |
|---:|---:|
| 11 | 151 |
| 5 | 48 |
| 9 | 9 |
| 10 | 99 |

`Exam`

| score | student_count |
|---:|---:|
| 975 | 10 |
| 966 | 60 |
| 844 | 76 |
| 749 | 76 |
| 744 | 100 |

Output:

| school_id | score |
|---:|---:|
| 5 | 975 |
| 9 | -1 |
| 10 | 749 |
| 11 | 744 |

School `10` can support the 76 students represented by scores `844` and `749`;
the smaller tied cutoff is `749`.

**Example 2**

- Input: `Schools = [(1, 10)]`, `Exam = [(900, 10), (800, 20)]`
- Output: `[(1, 900)]`

**Example 3**

- Input: `Schools = [(1, 4)]`, `Exam = [(900, 5)]`
- Output: `[(1, -1)]`

### Required Complexity
- **Time:** $O(SE)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

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

#### Complexity detail

Without a supporting index on `student_count`, the inequality join may compare
each of $S$ schools with all $E$ exam rows, taking $O(SE)$ time. Grouping keeps
one aggregate result per school, requiring $O(S)$ result or aggregation space.
Database engines may improve physical execution when additional indexes or
ordering are available, but the query does not assume them.

#### Alternatives and edge cases

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

</details>
