# Sudoku Solver

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 37 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Backtracking, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sudoku-solver/) |

## Problem Description
### Goal
You are given a partially filled $9 x 9$ Sudoku board with a valid, solvable set of clues. Replace every dot with a digit from `1` through `9` so that each row, each column, and each $3 x 3$ sub-box contains every digit exactly once.

All original clues must remain unchanged. The native method completes the supplied board in place and returns no value; the app returns the completed grid so its contents can be validated directly. The input guarantees a solution, so reporting impossibility is outside the contract.

### Function Contract
**Inputs**

- `board`: 9×9 `List[List[str]]` containing digits `1`–`9` or `.`

**Return value**

The solved `List[List[str]]`. App cases accept any valid completion preserving all clues; the platform artifact modifies `board` and returns `None`.

### Examples
**Example 1**

- Input: the standard partially filled puzzle in the cases
- Output: a valid completed board preserving every clue

**Example 2**

- Input: a board with one empty cell
- Output: the completed board

**Example 3**

- Input: an already solved board
- Output: the same board
