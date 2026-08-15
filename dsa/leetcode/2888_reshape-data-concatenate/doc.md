# Reshape Data: Concatenate

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2888 |
| Difficulty | Easy |
| Category | pandas |
| Topics | Uncategorized |
| Supported Languages | python |
| Official Link | [LeetCode](https://leetcode.com/problems/reshape-data-concatenate/) |

## Problem Description

### Goal

Two student DataFrames, `df1` and `df2`, share the same three-column schema: integer `student_id`, object `name`, and integer `age`. Each table contains a separate sequence of student rows.

Concatenate the tables vertically into one DataFrame. Every row from `df1` must appear first in its original order, followed by every row from `df2` in its original order. Preserve the shared column order and all cell values; the operation stacks rows rather than joining columns or matching records by an identifier.

### Function Contract

**Inputs**

- `df1`: A pandas DataFrame with columns `student_id`, `name`, and `age`.
- `df2`: A second pandas DataFrame with the same ordered columns and data types.

Let $n$ and $m$ be the numbers of rows in `df1` and `df2`, respectively.

**Return value**

Return one DataFrame containing the $n$ rows of `df1` followed by the $m$ rows of `df2`, with the shared three-column schema unchanged.

### Examples

#### Example 1

- **Input:** `df1 = [{"student_id": 1, "name": "Mason", "age": 8}, {"student_id": 2, "name": "Ava", "age": 6}, {"student_id": 3, "name": "Taylor", "age": 15}, {"student_id": 4, "name": "Georgia", "age": 17}]`, `df2 = [{"student_id": 5, "name": "Leo", "age": 7}, {"student_id": 6, "name": "Alex", "age": 7}]`
- **Output:** `[{"student_id": 1, "name": "Mason", "age": 8}, {"student_id": 2, "name": "Ava", "age": 6}, {"student_id": 3, "name": "Taylor", "age": 15}, {"student_id": 4, "name": "Georgia", "age": 17}, {"student_id": 5, "name": "Leo", "age": 7}, {"student_id": 6, "name": "Alex", "age": 7}]`

#### Example 2

- **Input:** `df1 = [{"student_id": 10, "name": "Mina", "age": 12}]`, `df2 = [{"student_id": 11, "name": "Bo", "age": 14}]`
- **Output:** `[{"student_id": 10, "name": "Mina", "age": 12}, {"student_id": 11, "name": "Bo", "age": 14}]`

#### Example 3

- **Input:** `df1 = [{"student_id": 7, "name": "Lee", "age": 9}, {"student_id": 3, "name": "Iris", "age": 16}]`, `df2 = [{"student_id": 7, "name": "Lee", "age": 9}]`
- **Output:** `[{"student_id": 7, "name": "Lee", "age": 9}, {"student_id": 3, "name": "Iris", "age": 16}, {"student_id": 7, "name": "Lee", "age": 9}]`
