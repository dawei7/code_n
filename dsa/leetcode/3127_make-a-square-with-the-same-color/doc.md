# Make a Square with the Same Color

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3127 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/make-a-square-with-the-same-color/) |

## Problem Description

### Goal

You are given a $3\times3$ matrix `grid` whose cells contain only `"B"` or `"W"`, representing black and white respectively. You may change the color of at most one cell; choosing not to change any cell is also allowed.

Determine whether this operation can make at least one contiguous $2\times2$ square have the same color in all four cells. Return `true` when such a square can already be found or can be created with one change, and return `false` otherwise.

### Function Contract

**Inputs**

- `grid`: Exactly three rows of three characters each, with every character equal to `"B"` or `"W"`.

**Return value**

Return a boolean indicating whether some contiguous $2\times2$ square can be made monochromatic by changing at most one cell.

### Examples

**Example 1**

- Input: `grid = [["B","W","B"],["B","W","W"],["B","W","B"]]`
- Output: `true`
- Explanation: Changing `grid[0][2]` to white makes the upper-right $2\times2$ square all white.

**Example 2**

- Input: `grid = [["B","W","B"],["W","B","W"],["B","W","B"]]`
- Output: `false`
- Explanation: Every $2\times2$ square has two cells of each color, so one change cannot make all four match.

**Example 3**

- Input: `grid = [["B","W","B"],["B","W","W"],["B","W","W"]]`
- Output: `true`
- Explanation: The lower-right $2\times2$ square is already entirely white.
