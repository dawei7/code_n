## Description

Table: `course_completions`

| Column Name | Type |
|---|---|
| `user_id` | integer |
| `course_id` | integer |
| `course_name` | varchar |
| `completion_date` | date |
| `course_rating` | integer |

The pair (`user_id`, `course_id`) uniquely identifies a row. Each row records one course completed by a user, the completion date, and that user's rating on the 1-to-5 scale.

Analyze the course histories to identify the learning transitions most often followed by top-performing students:

- A **top-performing student** has completed at least 5 courses and has an average `course_rating` of at least 4.
- For each such student, arrange the completed courses in chronological order.
- From that personal sequence, form every pair of consecutive courses, written as `Course A → Course B`.
- Count how often every ordered pair occurs across all top performers, revealing the most common transitions among high achievers.

Return each pair and its frequency. Sort higher frequencies first; when frequencies tie, sort by the first course name and then the second course name, both in ascending order.
