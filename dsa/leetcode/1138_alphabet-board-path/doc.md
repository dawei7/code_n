# Alphabet Board Path

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1138 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/alphabet-board-path/) |

## Problem Description

### Goal

The alphabet board is `['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy', 'z']`. A cursor begins on `a` at position `(0, 0)`. `U`, `D`, `L`, and `R` move one cell in the corresponding direction when that destination exists, and `!` appends the letter under the cursor to the answer.

Given a lowercase string `target`, return a minimum-length sequence of moves and selections whose appended letters equal `target`. Every move must remain on a lettered cell; in particular, the last row contains only `z` at column zero. When several minimum paths are valid, any one may be returned.

### Function Contract

**Inputs**

- `target`: a string of lowercase English letters with $1 \le \lvert\texttt{target}\rvert \le 100$.

Let $L=\lvert\texttt{target}\rvert$.

**Return value**

A minimum-length valid command string that selects the letters of `target` in order.

### Examples

**Example 1**

- Input: `target = "leet"`
- Output: `"DDR!UURRR!!DDD!"`

**Example 2**

- Input: `target = "code"`
- Output: `"RR!DDRR!UUL!R!"`
