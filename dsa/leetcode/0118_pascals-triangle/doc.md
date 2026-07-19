# Pascal's Triangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 118 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/pascals-triangle/) |

## Problem Description
### Goal
Given a positive integer `num_rows`, generate that many rows of Pascal's triangle. The triangle begins with the single value `1`; each later row contains one more entry than the row above it, starts and ends with `1`, and derives every interior entry from the two adjacent values above.

Return all rows in top-to-bottom order, with row lengths increasing from one through `num_rows`. Values must be represented as integers and grouped by row rather than flattened into one sequence. For example, requesting one row returns only `[[1]]`, while larger requests must preserve the triangle's symmetry and addition rule at every position.

### Function Contract
**Inputs**

- `num_rows`: the positive number of rows to generate

**Return value**

The triangle as a list of rows from top to bottom.

### Examples
**Example 1**

- Input: `num_rows = 5`
- Output: `[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]`

**Example 2**

- Input: `num_rows = 1`
- Output: `[[1]]`

**Example 3**

- Input: `num_rows = 3`
- Output: `[[1], [1, 1], [1, 2, 1]]`
