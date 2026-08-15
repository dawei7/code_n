# Create a DataFrame from List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2877 |
| Difficulty | Easy |
| Category | pandas |
| Topics | Uncategorized |
| Supported Languages | python |
| Official Link | [LeetCode](https://leetcode.com/problems/create-a-dataframe-from-list/) |

## Problem Description

### Goal

`student_data` is a two-dimensional list in which every row describes one student. The first value of a row is that student's identifier, and the second value is the student's age. Interpret the outer-list order as the required row order; the task does not ask for sorting or any other rearrangement.

Create and return a pandas `DataFrame` from those records. The result must have exactly two columns named `student_id` and `age`, in that order, and its rows must appear in the same order as the corresponding rows of `student_data`.

### Function Contract

**Inputs**

- `student_data`: A two-dimensional list whose rows have the form `[student_id, age]`.

**Return value**

A pandas `DataFrame` with columns `student_id` and `age`, preserving the input row order.

### Examples

#### Example 1

- **Input:** `student_data = [[1, 15], [2, 11], [3, 11], [4, 20]]`
- **Output:** a four-row DataFrame with columns `student_id` and `age` and rows `[1, 15]`, `[2, 11]`, `[3, 11]`, and `[4, 20]`.

#### Example 2

- **Input:** `student_data = [[42, 18]]`
- **Output:** a one-row DataFrame whose only row is `[42, 18]`.

#### Example 3

- **Input:** `student_data = [[9, 20], [2, 11], [7, 16]]`
- **Output:** a three-row DataFrame retaining the row order `9`, `2`, `7` in its `student_id` column.
