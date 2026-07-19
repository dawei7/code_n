# Transpose File

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 194 |
| Difficulty | Medium |
| Category | Shell |
| Topics | Shell |
| Supported Languages | bash |
| Official Link | [LeetCode](https://leetcode.com/problems/transpose-file/) |

## Problem Description
### Goal
The file `file.txt` contains a rectangular table: each input row has the same positive number of whitespace-separated fields. Transform the table so original rows become output columns and original columns become output rows.

Write the transposed table to standard output with one output row per original column and fields separated by single spaces. Preserve every field value exactly while changing only its position. If the input has `m` rows and `n` fields per row, the output must have `n` rows with `m` fields each. Do not print labels or expose this Bash task as function-return data.

### Function Contract
**Inputs**

- `file.txt`: rows containing the same positive number of whitespace-separated fields

**Return value**

Write one output row per original column, with fields separated by single spaces.

### Examples
**Example 1**

- File: rows `name age` and `alice 21`
- Output: rows `name alice` and `age 21`

**Example 2**

- File contains one row: `a b c`
- Output: three one-field rows

**Example 3**

- File contains one column
- Output: one row containing all original rows
