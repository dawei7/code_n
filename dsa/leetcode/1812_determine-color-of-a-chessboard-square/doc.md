# Determine Color of a Chessboard Square

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/determine-color-of-a-chessboard-square/) |
| Frontend ID | 1812 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A standard chessboard has files labeled from `"a"` through `"h"` and ranks labeled from `"1"` through `"8"`. Its square colors alternate horizontally and vertically, with `"a1"` black. Every pair of edge-adjacent squares therefore has opposite colors.

The two-character string `coordinates` names one valid square, with its file letter first and rank digit second. Return `true` when that square is white and `false` when it is black.

### Function Contract

**Inputs**

- `coordinates`: a string of length two.
- `coordinates[0]` is one lowercase letter from `"a"` through `"h"`.
- `coordinates[1]` is one digit from `"1"` through `"8"`.

**Return value**

- Return `true` if the named chessboard square is white.
- Return `false` if it is black.

### Examples

**Example 1**

- Input: `coordinates = "a1"`
- Output: `false`

The lower-left reference square is black.

**Example 2**

- Input: `coordinates = "h3"`
- Output: `true`

Its zero-based file and rank indices have different parity.

**Example 3**

- Input: `coordinates = "c7"`
- Output: `false`

Both zero-based indices are even, matching `"a1"`'s color.
