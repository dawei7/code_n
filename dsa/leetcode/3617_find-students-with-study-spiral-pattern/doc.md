# Find Students with Study Spiral Pattern

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3617 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-students-with-study-spiral-pattern/) |

## Problem Description

### Goal

The `students` table identifies students and their majors. The `study_sessions` table records each student's subject, session date, and studied hours. Order every student's sessions chronologically to obtain that student's subject sequence.

A study spiral uses at least three distinct subjects in a fixed repeating cycle. The sequence must contain at least two complete cycles, so it has at least twice as many sessions as subjects in the cycle. Every adjacent pair of ordered sessions must be no more than two days apart. For each qualifying student, report the cycle length and total hours across all sessions in the repeating sequence.

Return student identity and major with those two measures. Sort larger cycle lengths first and, when cycle lengths tie, sort larger total study hours first.

### Function Contract

**Inputs**

- `students`: rows with unique `student_id`, `student_name`, and `major` values.
- `study_sessions`: rows with unique `session_id`, a `student_id`, `subject`, `session_date`, and `hours_studied`.

Session order is determined by `session_date`, with `session_id` providing a deterministic order for sessions on the same date.

**Return value**

Return an ordered table with columns `student_id`, `student_name`, `major`, `cycle_length`, and `total_study_hours`. Include only students whose ordered sessions follow a repeating cycle of at least three subjects for at least two complete cycles and have no adjacent date gap greater than two days.

### Examples

#### Example 1

Alice studies `Math, Physics, Chemistry` twice in that order on consecutive dates. Her cycle length is `3` and her six sessions total `15.0` hours.

#### Example 2

Bob repeats a four-subject sequence twice, so his cycle length `4` places him before Alice's cycle length `3`.

#### Example 3

A student alternating only two subjects is excluded even when the alternation repeats, because a study spiral requires at least three distinct subjects.
