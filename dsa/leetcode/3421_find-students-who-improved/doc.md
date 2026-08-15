# Find Students Who Improved

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/find-students-who-improved/) |
| Frontend ID | 3421 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

The `Scores` table records a student's score for a subject on a particular exam date. For every student-and-subject pair with exams on at least two distinct dates, compare the score from its earliest date with the score from its latest date.

A pair shows improvement only when the latest score is strictly greater than the first score. Return one row for each improving pair with `student_id`, `subject`, `first_score`, and `latest_score`, ordered by `student_id` and then `subject`, both ascending. Scores between the endpoints do not determine eligibility.

### Function Contract

**Inputs**

- `Scores`: A table with integer `student_id`, text `subject`, integer `score`, and text `exam_date`. The composite primary key is `(student_id, subject, exam_date)`, and each score lies in $[0,100]$.

Let $r$ be the number of rows in `Scores`.

**Return value**

Return columns `student_id`, `subject`, `first_score`, and `latest_score` for pairs whose latest score is strictly higher than their earliest score. Sort the rows by `student_id` and `subject` ascending.

### Examples

#### Example 1

- **Input:** `Scores = [(101,"Math",70,"2023-01-15"),(101,"Math",85,"2023-02-15"),(101,"Physics",65,"2023-01-15"),(101,"Physics",60,"2023-02-15"),(102,"Math",80,"2023-01-15"),(102,"Math",85,"2023-02-15"),(103,"Math",90,"2023-01-15"),(104,"Physics",75,"2023-01-15"),(104,"Physics",85,"2023-02-15")]`
- **Output:** `[(101,"Math",70,85),(102,"Math",80,85),(104,"Physics",75,85)]`
- **Explanation:** The three returned pairs improve from their chronological first score to their chronological latest score. The Physics result for student 101 declines, and student 103 has only one exam.
