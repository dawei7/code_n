# Select Data

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2880 |
| Difficulty | Easy |
| Category | pandas |
| Topics | Uncategorized |
| Supported Languages | python |
| Official Link | [LeetCode](https://leetcode.com/problems/select-data/) |

## Problem Description

### Goal

The pandas `DataFrame` named `students` contains one row per student and has the columns `student_id`, `name`, and `age`. The identifier determines which record is requested; the order or values of the other rows must not affect the selection.

Find the student whose `student_id` equals `101`. Return a DataFrame containing that student's `name` and `age` only, with the output columns in exactly that order. Do not include `student_id` or unrelated student rows in the result.

### Function Contract

**Inputs**

- `students`: A pandas `DataFrame` with unique student identifiers and columns `student_id`, `name`, and `age`.

**Return value**

A one-row pandas `DataFrame` with columns `name` and `age` for the student whose identifier is `101`.

### Examples

**Example 1**

- Input: rows `[101, "Ulysses", 13]`, `[53, "William", 10]`, `[128, "Henry", 6]`, and `[3, "Henry", 11]`.
- Output: one row `[["Ulysses", 13]]` under columns `name` and `age`.

**Example 2**

- Input: the row with `student_id = 101` appears after another student.
- Output: the target student's `name` and `age`, regardless of position.

**Example 3**

- Input: the target row is the final row of the DataFrame.
- Output: that final student's `name` and `age` only.
