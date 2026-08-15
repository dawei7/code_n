# Number of Unique Subjects Taught by Each Teacher

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2356 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/) |

## Problem Description

### Goal

The `Teacher` table records teaching assignments at a university. Each row
identifies a teacher, a subject taught by that teacher, and the department in
which the assignment occurs. The pair `(subject_id, dept_id)` is the table's
primary key, so each subject-and-department assignment appears at most once.

For every teacher represented in the table, calculate how many distinct
subjects that teacher teaches. Teaching the same subject in multiple
departments contributes only one to that teacher's count. Return one row per
teacher with the required count; the result rows may appear in any order.

### Function Contract

**Input table**

- `Teacher(teacher_id, subject_id, dept_id)`: Teaching assignments whose three
  columns are integers and whose primary key is `(subject_id, dept_id)`.

Let $R$ be the number of rows in `Teacher`.

**Return value**

Return a table with columns `teacher_id` and `cnt`. Each teacher present in the
input appears once, and `cnt` is the number of distinct `subject_id` values
associated with that teacher. Row order is unrestricted.

### Examples

#### Example 1

Teacher 1 teaches subject 2 in two departments and subject 3 in one, so their
distinct-subject count is 2. Teacher 2 teaches four different subjects:

| teacher_id | cnt |
|---:|---:|
| 1 | 2 |
| 2 | 4 |
