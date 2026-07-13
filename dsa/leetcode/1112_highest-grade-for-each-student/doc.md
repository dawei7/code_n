# Highest Grade For Each Student

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1112 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [highest-grade-for-each-student](https://leetcode.com/problems/highest-grade-for-each-student/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/highest-grade-for-each-student/).

### Goal
For each student, report the course with their highest grade. If multiple courses share the highest grade, choose the course with the smallest `course_id`.

### Query Contract
**Input table**

- `Enrollments(student_id, course_id, grade)`: Course grade records.

**Output columns**

- `student_id`
- `course_id`
- `grade`

### Examples
**Example 1**

`Enrollments`

| student_id | course_id | grade |
|---:|---:|---:|
| 2 | 2 | 95 |
| 2 | 3 | 95 |
| 1 | 1 | 90 |
| 1 | 2 | 99 |

Output:

| student_id | course_id | grade |
|---:|---:|---:|
| 1 | 2 | 99 |
| 2 | 2 | 95 |

---

## Solution
### Approach
Rank each student's rows by `grade` descending and `course_id` ascending, then keep the first-ranked row for each student.

A window function such as `ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY grade DESC, course_id ASC)` captures both the maximum-grade rule and the tie-breaker.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query partitions enrollment rows by student and orders each partition.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
