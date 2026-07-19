# Check if Word Can Be Placed In Crossword

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2018 |
| Difficulty | Medium |
| Topics | Array, Matrix, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/) |

## Problem Description

### Goal

The crossword board contains lowercase letters, spaces representing empty
cells, and `#` characters representing blocked cells.

Determine whether `word` can occupy one horizontal or vertical slot, in either
forward or backward order. Every occupied cell must be non-blocked and either
blank or already contain the required letter. The cells immediately before
and after the word along its direction must be outside the board or blocked;
therefore, the word must fill an entire maximal non-blocked slot rather than
only part of a longer run.

### Function Contract

Let $R$ and $C$ be the board's row and column counts.

**Inputs**

- `board`: an $R\times C$ matrix whose cells are spaces, `#`, or lowercase
  English letters, with $1\le RC\le2\cdot10^5$.
- `word`: a lowercase string of length from $1$ through $\max(R,C)$.

**Return value**

Return `true` if at least one complete horizontal or vertical slot accepts the
word in either direction; otherwise return `false`.

### Examples

**Example 1**

- Input: `board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"`
- Output: `true`
- Explanation: The word fits vertically from top to bottom.

**Example 2**

- Input: `board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"`
- Output: `false`
- Explanation: Each possible vertical run is longer than the word or contains
  incompatible letters.

**Example 3**

- Input: `board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"`
- Output: `true`
- Explanation: The word fits horizontally from right to left.
