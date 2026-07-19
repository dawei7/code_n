# Count Student Number in Departments

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 580 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/count-student-number-in-departments/) |

## Problem Description
### Goal
Given a `Department` table containing the complete department catalog and a `Student` table whose `dept_id` identifies each student's department, count how many students belong to every department. A department must still appear when no student row refers to it, with its count reported as zero.

Return the columns `dept_name` and `student_number`. Order the result by `student_number` in descending order so departments with more students appear first; when two departments have the same count, order their names in ascending lexicographical order.

### Function Contract
**Inputs**

- `Student(student_id, student_name, gender, dept_id)`: students and their department identifiers
- `Department(dept_id, dept_name)`: the complete department catalog

**Return value**

- Columns `dept_name` and `student_number`
- Include one row for every department, using zero when no student belongs to it
- Order by `student_number` descending, then `dept_name` ascending

### Examples
**Example 1**

- Input: Engineering has three students and History has one
- Output: Engineering with `3`, then History with `1`

**Example 2**

- Input: Music has no students
- Output: Music with `0`

**Example 3**

- Input: Art and Biology have the same student count
- Output: Art before Biology
