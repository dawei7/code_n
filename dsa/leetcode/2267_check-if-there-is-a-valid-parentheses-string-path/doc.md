# Check if There Is a Valid Parentheses String Path

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2267 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/) |

## Problem Description

### Goal

A nonempty parentheses string is valid when its parentheses can be matched in
the usual nested or concatenated form: `()` is valid, two valid strings may be
concatenated, and enclosing a valid string in one pair of parentheses remains
valid.

The matrix `grid` contains only `(` and `)`. Begin at its upper-left cell
`(0, 0)` and reach the bottom-right cell `(m - 1, n - 1)`, moving only one
cell down or one cell right at each step. Reading the visited characters in
path order produces a parentheses string.

Return whether at least one such monotone path produces a valid parentheses
string.

### Function Contract

**Inputs**

- `grid`: An $m\times n$ matrix whose entries are `(` or `)`.

Both dimensions satisfy $1\le m,n\le100$. Every path contains exactly
$m+n-1$ cells.

**Return value**

Return `true` if some upper-left-to-bottom-right path, using only down and
right moves, spells a valid parentheses string. Otherwise return `false`.

### Examples

#### Example 1

- **Input:** `grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]`
- **Output:** `true`

Among the possible paths are ones spelling `()(())` and `((()))`.

#### Example 2

- **Input:** `grid = [[")",")"],["(","("]]`
- **Output:** `false`

The two paths spell `"))("` and `")(("`, neither of which is valid.
