# Drop Missing Data

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2883 |
| Difficulty | Easy |
| Category | pandas |
| Topics | Uncategorized |
| Supported Languages | python |
| Official Link | [LeetCode](https://leetcode.com/problems/drop-missing-data/) |

## Problem Description

### Goal

A student DataFrame contains the columns `student_id`, `name`, and `age`. Some records have a missing value in the `name` column, so those rows do not provide the required student name.

Remove every row whose `name` is missing and return the remaining student records. Keep all three original columns and preserve the order and values of every retained row. The filtering condition applies specifically to the presence of a student name.

### Function Contract

**Inputs**

- `students`: A pandas DataFrame with integer columns `student_id` and `age`, plus object column `name`; some `name` values may be missing.

Let $n$ be the number of student rows.

**Return value**

Return a DataFrame containing exactly the rows whose `name` value is present, with the original columns and relative row order unchanged.

### Examples

#### Example 1

- **Input:** `students = [{"student_id": 32, "name": "Piper", "age": 5}, {"student_id": 217, "name": null, "age": 19}, {"student_id": 779, "name": "Georgia", "age": 20}, {"student_id": 849, "name": "Willow", "age": 14}]`
- **Output:** `[{"student_id": 32, "name": "Piper", "age": 5}, {"student_id": 779, "name": "Georgia", "age": 20}, {"student_id": 849, "name": "Willow", "age": 14}]`

#### Example 2

- **Input:** `students = [{"student_id": 1, "name": "Ada", "age": 18}, {"student_id": 2, "name": "Bo", "age": 20}]`
- **Output:** `[{"student_id": 1, "name": "Ada", "age": 18}, {"student_id": 2, "name": "Bo", "age": 20}]`

#### Example 3

- **Input:** `students = [{"student_id": 3, "name": null, "age": 16}, {"student_id": 4, "name": null, "age": 18}, {"student_id": 5, "name": null, "age": 21}]`
- **Output:** `[]`
