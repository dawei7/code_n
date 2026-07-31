# Get the Size of a DataFrame

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2878 |
| Difficulty | Easy |
| Category | pandas |
| Topics | Uncategorized |
| Supported Languages | python |
| Official Link | [LeetCode](https://leetcode.com/problems/get-the-size-of-a-dataframe/) |

## Problem Description

### Goal

The pandas `DataFrame` named `players` contains one player per row and stores player attributes in columns such as `player_id`, `name`, `age`, `position`, and `team`. Its exact dimensions are determined by the supplied table rather than by the values stored in any particular column.

Determine the number of rows and the number of columns in `players`. Return those two dimensions as an array in the fixed order `[number of rows, number of columns]`; do not return the total number of cells or count only non-null values.

### Function Contract

**Inputs**

- `players`: A pandas `DataFrame` containing the player records and their attributes.

**Return value**

A two-element integer list `[row_count, column_count]`.

### Examples

**Example 1**

- Input: a `players` DataFrame containing 10 rows and the five columns `player_id`, `name`, `age`, `position`, and `team`.
- Output: `[10, 5]`

**Example 2**

- Input: a one-row `players` DataFrame with the same five columns.
- Output: `[1, 5]`

**Example 3**

- Input: a three-row `players` DataFrame with the same five columns.
- Output: `[3, 5]`
