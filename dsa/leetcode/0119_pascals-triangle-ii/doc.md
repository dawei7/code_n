# Pascal's Triangle II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 119 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/pascals-triangle-ii/) |

## Problem Description
### Goal
Given a nonnegative zero-based index `row_index`, return exactly that row of Pascal's triangle. Row `0` is `[1]`; every subsequent row begins and ends with `1`, and each interior entry is the sum of the two neighboring entries from the preceding row.

The result must contain `row_index + 1` integers in left-to-right order. Return only the requested row rather than the complete triangle, while preserving the standard symmetric binomial-coefficient values even for the largest allowed index. In particular, index `1` produces `[1, 1]`, and no special padding or placeholder entries belong outside the row's two boundary values.

### Function Contract
**Inputs**

- `row_index`: the zero-based row index

**Return value**

The `row_index + 1` binomial coefficients from left to right.

### Examples
**Example 1**

- Input: `row_index = 3`
- Output: `[1, 3, 3, 1]`

**Example 2**

- Input: `row_index = 0`
- Output: `[1]`

**Example 3**

- Input: `row_index = 5`
- Output: `[1, 5, 10, 10, 5, 1]`
