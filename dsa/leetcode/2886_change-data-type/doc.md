# Change Data Type

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2886 |
| Difficulty | Easy |
| Category | pandas |
| Topics | Uncategorized |
| Supported Languages | python |
| Official Link | [LeetCode](https://leetcode.com/problems/change-data-type/) |

## Problem Description

### Goal

A student DataFrame contains the columns `student_id`, `name`, `age`, and `grade`. The first and third columns store integers, names are objects, and `grade` is currently stored with the float data type even though its values represent integer grades.

Correct that schema error by converting only the `grade` column to an integer data type. Return the student table with the same four columns, rows, order, and values, except that every grade is represented as an integer rather than a float.

### Function Contract

**Inputs**

- `students`: A pandas DataFrame with integer columns `student_id` and `age`, an object column `name`, and a float column `grade` whose values are integer-valued.

Let $n$ be the number of student rows.

**Return value**

Return the student DataFrame with `grade` converted to an integer data type and all other data preserved.

### Examples

**Example 1**

- Input: `students = [{"student_id": 1, "name": "Ava", "age": 6, "grade": 73.0}, {"student_id": 2, "name": "Kate", "age": 15, "grade": 87.0}]`
- Output: `[{"student_id": 1, "name": "Ava", "age": 6, "grade": 73}, {"student_id": 2, "name": "Kate", "age": 15, "grade": 87}]`

**Example 2**

- Input: `students = [{"student_id": 9, "name": "Mina", "age": 18, "grade": 100.0}]`
- Output: `[{"student_id": 9, "name": "Mina", "age": 18, "grade": 100}]`

**Example 3**

- Input: `students = [{"student_id": 20, "name": "Noah", "age": 7, "grade": 0.0}, {"student_id": 8, "name": "Iris", "age": 13, "grade": 55.0}]`
- Output: `[{"student_id": 20, "name": "Noah", "age": 7, "grade": 0}, {"student_id": 8, "name": "Iris", "age": 13, "grade": 55}]`
