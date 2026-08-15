# Match Alphanumerical Pattern in Matrix I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3078 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/match-alphanumerical-pattern-in-matrix-i/) |

## Problem Description

### Goal

You are given a rectangular integer matrix `board`, whose cells are digits from $0$ through $9$, and a rectangular string matrix `pattern`. Every character in `pattern` is either a decimal digit or a lowercase English letter.

A submatrix of `board` matches `pattern` when both have the same dimensions and every pattern cell can be interpreted consistently. A digit character is a fixed literal, so it must equal the corresponding board digit. Every occurrence of the same letter must correspond to the same digit, while two distinct letters must correspond to different digits. Letter assignments are compared with other letter assignments; a letter may use a digit that also appears as a fixed literal elsewhere in the pattern.

Find a matching submatrix and return the row and column of its upper-left cell. If several matches exist, choose the one with the smallest row; within that row, choose the smallest column. If no match exists, return `[-1, -1]`.

### Function Contract

**Inputs**

- `board`: An $R \times C$ integer matrix whose entries lie from $0$ through $9$.
- `pattern`: A list of $p$ equal-length strings, each of length $q$, containing only digits and lowercase English letters.

The dimensions satisfy $1 \le R,C,p,q \le 50$.

**Return value**

- `[row, column]` for the row-major earliest matching $p \times q$ submatrix, or `[-1, -1]` when no placement matches.

### Examples

#### Example 1

- **Input:** `board = [[1, 2, 2], [2, 2, 3], [2, 3, 3]]`, `pattern = ["ab", "bb"]`
- **Output:** `[0, 0]`
- **Explanation:** At `(0, 0)`, assigning `a` to `1` and `b` to `2` produces the selected board region. Another match begins at `(1, 1)`, but row-major order selects `(0, 0)`.

#### Example 2

- **Input:** `board = [[1, 1, 2], [3, 3, 4], [6, 6, 6]]`, `pattern = ["ab", "66"]`
- **Output:** `[1, 1]`
- **Explanation:** The placement at `(1, 1)` maps `a` to `3` and `b` to `4`, while both literal `6` cells match exactly. The placement at `(1, 0)` fails because distinct letters would both receive digit `3`.

#### Example 3

- **Input:** `board = [[1, 2], [2, 1]]`, `pattern = ["xx"]`
- **Output:** `[-1, -1]`
- **Explanation:** The repeated letter requires two equal adjacent digits, which neither row contains.
