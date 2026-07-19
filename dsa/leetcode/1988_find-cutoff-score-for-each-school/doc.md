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
