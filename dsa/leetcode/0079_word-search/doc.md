# Word Search

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 79 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Backtracking, Depth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/word-search/) |

## Problem Description
### Goal
You are given a rectangular board of characters and a nonempty target `word`. Starting from any cell, trace the word in order by moving between horizontally or vertically adjacent cells for each next character; diagonal moves are not allowed.

Return whether at least one such path spells the entire word. A board cell may be used at most once within the same path, although different attempted paths may reuse it. Characters cannot be skipped, and the path may turn in any orthogonal direction between steps.

### Function Contract
**Inputs**

- `board`: a nonempty rectangular matrix of characters
- `word`: the nonempty target string

**Return value**

`True` when at least one valid cell path spells `word`, otherwise `False`.

### Examples
**Example 1**

- Input: `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"`
- Output: `True`

**Example 2**

- Input: the same board, `word = "SEE"`
- Output: `True`

**Example 3**

- Input: the same board, `word = "ABCB"`
- Output: `False`
