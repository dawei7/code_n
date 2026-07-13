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

### Required Complexity

- **Time:** $O(mn + q)$
- **Space:** $O(mn)$

<details>
<summary>Approach</summary>

#### General

**Give every grid boundary a two-dimensional prefix value**

Build a matrix `prefix` with one extra top row and left column of zeroes. Entry `prefix[r][c]` stores the sum of the original rectangle from $(0,0)$ through $(r-1,c-1)$.

For a new cell, combine the prefix above it and the prefix to its left, subtract their overlap, then add the cell:
`prefix[r + 1][c + 1] = value + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]`.

**Inclusion–exclusion isolates any requested rectangle**

For inclusive corners `(row1,col1)` and `(row2,col2)`, begin with the prefix through the lower-right boundary. Subtract the region above the query and the region left of it. Their upper-left overlap was subtracted twice, so add that overlap back once.

The formula is:
`prefix[row2 + 1][col2 + 1] - prefix[row1][col2 + 1] - prefix[row2 + 1][col1] + prefix[row1][col1]`.

The zero border makes queries touching the top or left image edge use the identical formula.

**Every cell receives coefficient one exactly when it is inside**

Consider a matrix cell relative to the requested rectangle. A cell inside lies in the large lower-right prefix but in neither removed strip, so its coefficient is one. A cell solely above or left is canceled by the corresponding subtraction. A cell in the upper-left overlap appears in the large prefix, both subtractions, and the added overlap, giving coefficient $1 - 1 - 1 + 1 = 0$. Thus precisely the requested cells remain.

#### Complexity detail

Constructing all $(m + 1)(n + 1)$ prefix entries takes $O(mn)$ time and space. Each of the `q` queries performs four reads and constant arithmetic, so total time is $O(mn + q)$. Returned sums are output storage.

#### Alternatives and edge cases

- **Scan each rectangle directly:** is correct but can cost $O(mn)$ per query and $O(qmn)$ overall.
- **One-dimensional prefix sums per row:** reduce each query to $O(number of rows)$, but the full 2D prefix achieves constant query time.
- Single-cell, single-row, single-column, and full-matrix rectangles all use the same inclusion–exclusion formula. Negative entries require no special case.

</details>
