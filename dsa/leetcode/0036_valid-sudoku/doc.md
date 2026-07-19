# Valid Sudoku

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 36 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-sudoku/) |

## Problem Description
### Goal
You are given a partially filled $9 x 9$ Sudoku board. Filled cells contain digits `1` through `9`, while a dot represents an empty cell. Check the values already present against the standard Sudoku constraints.

No digit may appear twice in one row, one column, or one of the nine $3 x 3$ sub-boxes. Empty cells impose no conflict and do not need to be filled. Return whether the current board is valid; validity does not require proving that the unfinished puzzle has a solution.

### Function Contract
**Inputs**

- `board`: 9×9 `List[List[str]]` containing digits `1`–`9` or `.`

**Return value**

`True` when no filled digit is duplicated in any required unit; otherwise `False`.

### Examples
**Example 1**

- Input: the standard partially filled valid board shown in the cases
- Output: `True`

**Example 2**

- Input: the same board with a second `5` in its first row
- Output: `False`

**Example 3**

- Input: an empty 9×9 board
- Output: `True`
