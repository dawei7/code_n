# Valid Sudoku

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_17` |
| Frontend ID | 36 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Matrix |
| Official Link | [valid-sudoku](https://leetcode.com/problems/valid-sudoku/) |

## Problem Description & Examples
### Goal
Determine if a 9x9 Sudoku board is valid. A board is valid if:
- Each row contains digits 1-9 without repetition.
- Each column contains digits 1-9 without repetition.
- Each of the nine 3x3 sub-boxes contains digits 1-9 without repetition.

Empty cells are represented as `"."`.

`solve(board)` receives a 9x9 list and returns `True` or `False`.

### Function Contract
**Inputs**

- `board`: List[List[str]] - 9x9 board with digits 1-9 or '.'

**Return value**

bool - True if the board is valid

### Examples
**Example 1**

- Input: `board = <9x9 grid>`
- Output: `True`

**Example 2**

- Input: `board = [['.', '.', '.', '9', '.', '.', '.', '.', ...], ['.', '3', '2', '.', '9', '.', '.', '.', ...], ['.', '.', '.', '.', '7', '.', '.', '9', ...], ['.', '9', '.', '7', '.', '.', '.', '.', ...], ['.', '.', '.', '4', '3', '.', '.', '6', ...], ['.', '.', '.', '2', '.', '.', '.', '.', ...], ['.', '.', '.', '.', '.', '4', '.', '5', ...], ['3', '.', '.', '.', '.', '.', '.', '.', ...], ...]`
- Output: `False`

**Example 3**

- Input: `board = [['2', '8', '.', '.', '.', '8', '7', '.', ...], ['8', '4', '.', '6', '1', '.', '7', '.', ...], ['.', '.', '.', '.', '.', '.', '.', '.', ...], ['.', '.', '.', '.', '5', '6', '.', '.', ...], ['.', '.', '.', '5', '.', '.', '.', '.', ...], ['4', '.', '.', '.', '.', '.', '.', '.', ...], ['3', '.', '.', '.', '1', '.', '.', '.', ...], ['.', '4', '.', '.', '.', '.', '9', '.', ...], ...]`
- Output: `False`

---

## Underlying Base Algorithm(s)
- [Two Sum / hash lookup](hash_01_two-sum.md)
- [Grouping by hash key](hash_04_group-anagrams.md)
- [Set-based sequence reasoning](hash_06_longest-consecutive-sequence.md)

---

## Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
