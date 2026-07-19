# Range Sum Query 2D - Immutable

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 304 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Design, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/range-sum-query-2d-immutable/) |

## Problem Description
### Goal
Construct a `NumMatrix` from a nonempty rectangular integer matrix that remains unchanged. Repeated queries provide upper-left coordinates `(row1, col1)` and lower-right coordinates `(row2, col2)` for a valid axis-aligned subrectangle.

Return the sum of every matrix value inside each rectangle, including all four boundary rows and columns. Negative values and overlapping query regions are allowed. Preprocess the matrix so later `sumRegion` calls run in constant time rather than revisiting every enclosed cell. The app adapter collects results in query order, while the native object retains the same immutable data across calls.

### Function Contract
**Inputs**

- `matrix`: a nonempty rectangular integer matrix
- `queries`: a list of `[row1, col1, row2, col2]` rectangles with valid inclusive corners

**Return value**

A list containing the sum inside each requested rectangle, in query order.

### Examples
**Example 1**

- Input: `matrix = [[3,0],[1,2]], queries = [[0,0,1,1]]`
- Output: `[6]`

**Example 2**

- Input: `matrix = [[-2,94],[7,-90]], queries = [[1,1,1,1]]`
- Output: `[-90]`

**Example 3**

- Input: `matrix = [[-66,45],[95,-84]], queries = [[1,0,1,1]]`
- Output: `[11]`
