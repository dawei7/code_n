# Rename Columns

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2885 |
| Difficulty | Easy |
| Category | pandas |
| Topics | Uncategorized |
| Supported Languages | python |
| Official Link | [LeetCode](https://leetcode.com/problems/rename-columns/) |

## Problem Description

### Goal

A student DataFrame has four columns named `id`, `first`, `last`, and `age`. Its row values are already correct, but each column must receive a more descriptive name.

Rename `id` to `student_id`, `first` to `first_name`, `last` to `last_name`, and `age` to `age_in_years`. Return the resulting DataFrame with those four columns in the same order, preserving every student row and every stored value; this task changes labels only, not the data itself.

### Function Contract

**Inputs**

- `students`: A pandas DataFrame with integer columns `id` and `age`, plus object columns `first` and `last`.

Let $n$ be the number of student rows.

**Return value**

Return the same student data under the ordered columns `student_id`, `first_name`, `last_name`, and `age_in_years`.

### Examples

**Example 1**

- Input: `students = [{"id": 1, "first": "Mason", "last": "King", "age": 6}, {"id": 2, "first": "Ava", "last": "Wright", "age": 7}, {"id": 3, "first": "Taylor", "last": "Hall", "age": 16}, {"id": 4, "first": "Georgia", "last": "Thompson", "age": 18}, {"id": 5, "first": "Thomas", "last": "Moore", "age": 10}]`
- Output: `[{"student_id": 1, "first_name": "Mason", "last_name": "King", "age_in_years": 6}, {"student_id": 2, "first_name": "Ava", "last_name": "Wright", "age_in_years": 7}, {"student_id": 3, "first_name": "Taylor", "last_name": "Hall", "age_in_years": 16}, {"student_id": 4, "first_name": "Georgia", "last_name": "Thompson", "age_in_years": 18}, {"student_id": 5, "first_name": "Thomas", "last_name": "Moore", "age_in_years": 10}]`

**Example 2**

- Input: `students = [{"id": 9, "first": "Ada", "last": "Lovelace", "age": 17}]`
- Output: `[{"student_id": 9, "first_name": "Ada", "last_name": "Lovelace", "age_in_years": 17}]`

**Example 3**

- Input: `students = [{"id": 10, "first": "Lee", "last": "Kim", "age": 12}, {"id": 11, "first": "Lee", "last": "Park", "age": 15}]`
- Output: `[{"student_id": 10, "first_name": "Lee", "last_name": "Kim", "age_in_years": 12}, {"student_id": 11, "first_name": "Lee", "last_name": "Park", "age_in_years": 15}]`
